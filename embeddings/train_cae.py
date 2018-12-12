#!/usr/bin/env python

"""
Train a recurrent correspondence autoencoder.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2018
"""

from __future__ import division
from __future__ import print_function
from datetime import datetime
from os import path
from scipy.spatial.distance import pdist
import argparse
import cPickle as pickle
import hashlib
import numpy as np
import os
import sys
import tensorflow as tf

sys.path.append(path.join("..", "src"))

from tflego import NP_DTYPE, TF_DTYPE, NP_ITYPE, TF_ITYPE
import batching
import data_io
import samediff
import tflego
import training


#-----------------------------------------------------------------------------#
#                           DEFAULT TRAINING OPTIONS                          #
#-----------------------------------------------------------------------------#

default_options_dict = {
        "data_dir": path.join("data", "buckeye.mfcc"),
        "train_tag": "utd",                 # "gt", "gt2", "utd", "rnd"
        "max_length": 100,
        "min_length": 50,                   # only used with "rnd" train_tag
        "bidirectional": False,
        "rnn_type": "gru",                  # "lstm", "gru", "rnn"
        "enc_n_hiddens": [400, 400, 400],
        "dec_n_hiddens": [400, 400, 400],
        "n_z": 130,                         # latent dimensionality
        "learning_rate": 0.001,
        "keep_prob": 1.0,
        "ae_n_epochs": 100,                 # AE pretraining options
        "ae_batch_size": 300,
        "ae_n_buckets": 3,
        "pretrain_usefinal": False,         # if True, do not use best
                                            # validation AE model, but rather
                                            # use final model
        "cae_n_epochs": 10,                 # CAE training options
        "cae_batch_size": 300,
        "cae_n_buckets": 3,
        "extrinsic_usefinal": False,        # if True, during final extrinsic
                                            # evaluation, the final saved model
                                            # will be used (instead of the
                                            # validation best)
        "use_test_for_val": False,
        "n_val_interval": 1,
        "d_speaker_embedding": 10,           # if None, no speaker information
                                            # is used, otherwise this is the
                                            # embedding dimensionality
        "rnd_seed": 1,
    }


#-----------------------------------------------------------------------------#
#                              TRAINING FUNCTIONS                             #
#-----------------------------------------------------------------------------#

def build_cae_from_options_dict(a, a_lengths, b_lengths, options_dict):

    # Latent layer
    build_latent_func = tflego.build_autoencoder
    latent_func_kwargs = {
        "enc_n_hiddens": [],
        "n_z": options_dict["n_z"],
        "dec_n_hiddens": [options_dict["dec_n_hiddens"][0]],
        "activation": tf.nn.relu
        }

    # Speaker embedding
    if options_dict["d_speaker_embedding"] is not None:
        speaker_id = tf.placeholder(TF_ITYPE, [None])
        with tf.variable_scope("speaker_embedding"):
            speaker_embedding = tf.get_variable(
                    "E", [options_dict["n_speakers"],
                    options_dict["d_speaker_embedding"]], dtype=TF_DTYPE,
                    initializer=tf.contrib.layers.xavier_initializer()
                    )
            embedding_lookup = tf.nn.embedding_lookup(
                speaker_embedding, speaker_id
                )

    # Network
    network_dict = tflego.build_multi_encdec_lazydynamic_latentfunc(
        a, a_lengths, options_dict["enc_n_hiddens"],
        options_dict["dec_n_hiddens"], build_latent_func, latent_func_kwargs,
        y_lengths=b_lengths, rnn_type=options_dict["rnn_type"],
        bidirectional=options_dict["bidirectional"],
        keep_prob=options_dict["keep_prob"],
        add_conditioning_tensor=None if options_dict["d_speaker_embedding"] is
        None else embedding_lookup
        )

    encoder_states = network_dict["encoder_states"]
    ae = network_dict["latent_layer"]
    z = ae["z"]
    y = network_dict["decoder_output"]
    mask = network_dict["mask"]
    y *= tf.expand_dims(mask, -1)  # safety

    if options_dict["d_speaker_embedding"] is not None:
        return {
            "z": z, "y": y, "mask": mask, "speaker_id": speaker_id,
            "speaker_embedding": speaker_embedding
            }
    else:
        return {"z": z, "y": y, "mask": mask}


def train_cae(options_dict):
    """Train and save a CAE."""

    # PRELIMINARY
    assert (options_dict["train_tag"] != "rnd") or \
        (options_dict["cae_n_epochs"] == 0), \
        "random segment training only possible with AE (cae_n_epochs=0)"
    print(datetime.now())

    # Output directory
    hasher = hashlib.md5(repr(sorted(options_dict.items())).encode("ascii"))
    # hash_str = (
    #     datetime.now().strftime("%y%m%d.%Hh%M") + "." +
    #     # datetime.now().strftime("%y%m%d.%Hh%Mm%Ss") + "." +
    #     hasher.hexdigest()[:5]
    #     )
    hash_str = hasher.hexdigest()[:10]
    model_dir = path.join(
        "models", path.split(options_dict["data_dir"])[-1] + "." +
        options_dict["train_tag"], options_dict["script"], hash_str
        )
    options_dict_fn = path.join(model_dir, "options_dict.pkl")
    print("Model directory:", model_dir)
    if not os.path.isdir(model_dir):
        os.makedirs(model_dir)
    print("Options:", options_dict)

    # Random seeds
    # random.seed(options_dict["rnd_seed"])
    np.random.seed(options_dict["rnd_seed"])
    tf.set_random_seed(options_dict["rnd_seed"])


    # LOAD AND FORMAT DATA

    # Training data
    train_tag = options_dict["train_tag"]
    min_length = None
    if options_dict["train_tag"] == "rnd":
        min_length = options_dict["min_length"]
        train_tag = "all"
    npz_fn = path.join(
        options_dict["data_dir"], "train." + train_tag + ".npz"
        )
    train_x, train_labels, train_lengths, train_keys, train_speakers = (
        data_io.load_data_from_npz(npz_fn, min_length)
        )

    # Validation data
    if options_dict["use_test_for_val"]:
        npz_fn = path.join(options_dict["data_dir"], "test.npz")
    else:
        npz_fn = path.join(options_dict["data_dir"], "val.npz")
    val_x, val_labels, val_lengths, val_keys, val_speakers = (
        data_io.load_data_from_npz(npz_fn)
        )

    # Convert training speakers, if speaker embeddings
    if options_dict["d_speaker_embedding"] is not None:
        train_speaker_set = set(train_speakers)
        speaker_to_id = {}
        id_to_speaker = {}
        for i, speaker in enumerate(sorted(list(train_speaker_set))):
            speaker_to_id[speaker] = i
            id_to_speaker[i] = speaker
        train_speaker_ids = []
        for speaker in train_speakers:
            train_speaker_ids.append(speaker_to_id[speaker])
        train_speaker_ids = np.array(train_speaker_ids, dtype=NP_ITYPE)
        options_dict["n_speakers"] = max(speaker_to_id.values()) + 1

    # Truncate and limit dimensionality
    max_length = options_dict["max_length"]
    d_frame = 13  # None
    options_dict["n_input"] = d_frame
    print("Limiting dimensionality:", d_frame)
    print("Limiting length:", max_length)
    data_io.trunc_and_limit_dim(train_x, train_lengths, d_frame, max_length)
    data_io.trunc_and_limit_dim(val_x, val_lengths, d_frame, max_length)

    # Get pairs
    pair_list = batching.get_pair_list(train_labels)


    # DEFINE MODEL

    print(datetime.now())
    print("Building model")

    # Model filenames
    pretrain_intermediate_model_fn = path.join(model_dir, "ae.tmp.ckpt")
    pretrain_model_fn = path.join(model_dir, "ae.best_val.ckpt")
    intermediate_model_fn = path.join(model_dir, "cae.tmp.ckpt")
    model_fn = path.join(model_dir, "cae.best_val.ckpt")

    # Model graph
    a = tf.placeholder(TF_DTYPE, [None, None, options_dict["n_input"]])
    a_lengths = tf.placeholder(TF_ITYPE, [None])
    b = tf.placeholder(TF_DTYPE, [None, None, options_dict["n_input"]])
    b_lengths = tf.placeholder(TF_ITYPE, [None])
    network_dict = build_cae_from_options_dict(
        a, a_lengths, b_lengths, options_dict
        )
    mask = network_dict["mask"]
    z = network_dict["z"]
    y = network_dict["y"]
    if options_dict["d_speaker_embedding"] is not None:
        speaker_id = network_dict["speaker_id"]

    # Reconstruction loss
    loss = tf.reduce_mean(
        tf.reduce_sum(tf.reduce_mean(tf.square(b - y), -1), -1) /
        tf.reduce_sum(mask, 1)
        )  # https://danijar.com/variable-sequence-lengths-in-tensorflow/
    # # Temp
    # alpha = 0.1
    # loss += alpha*tf.reduce_mean(
    #     tf.reduce_sum(tf.reduce_mean(tf.square(a - y), -1), -1) /
    #     tf.reduce_sum(mask, 1)
    #     )  # temp
    optimizer = tf.train.AdamOptimizer(
        learning_rate=options_dict["learning_rate"]
        ).minimize(loss)


    # AUTOENCODER PRETRAINING: TRAIN AND VALIDATE

    print(datetime.now())
    print("Pretraining model")

    # Validation function
    def samediff_val(normalise=True):
        # Embed validation
        np.random.seed(options_dict["rnd_seed"])
        val_batch_iterator = batching.SimpleIterator(val_x, len(val_x), False)
        labels = [val_labels[i] for i in val_batch_iterator.indices]
        saver = tf.train.Saver()
        with tf.Session() as session:
            saver.restore(session, val_model_fn)
            for batch_x_padded, batch_x_lengths in val_batch_iterator:
                np_x = batch_x_padded
                np_x_lengths = batch_x_lengths
                np_z = session.run(
                    [z], feed_dict={a: np_x, a_lengths: np_x_lengths}
                    )[0]
                break  # single batch

        embed_dict = {}
        for i, utt_key in enumerate(
                [val_keys[i] for i in val_batch_iterator.indices]):
            embed_dict[utt_key] = np_z[i]

        # Same-different
        if normalise:
            np_z_normalised = (np_z - np_z.mean(axis=0))/np_z.std(axis=0)
            distances = pdist(np_z_normalised, metric="cosine")
            matches = samediff.generate_matches_array(labels)
            ap, prb = samediff.average_precision(
                distances[matches == True], distances[matches == False]
                )
        else:
            distances = pdist(np_z, metric="cosine")
            matches = samediff.generate_matches_array(labels)
            ap, prb = samediff.average_precision(
                distances[matches == True], distances[matches == False]
                )    
        return [prb, -ap]

    # Train AE
    val_model_fn = pretrain_intermediate_model_fn
    if options_dict["train_tag"] == "rnd":
        train_batch_iterator = batching.RandomSegmentsIterator(
            train_x, options_dict["ae_batch_size"],
            options_dict["ae_n_buckets"], shuffle_every_epoch=True,
            paired=True
            )
    else:
        train_batch_iterator = batching.PairedBucketIterator(
            train_x, [(i, i) for i in xrange(len(train_x))],
            options_dict["ae_batch_size"], options_dict["ae_n_buckets"],
            shuffle_every_epoch=True, speaker_ids=None if
            options_dict["d_speaker_embedding"] is None else train_speaker_ids
            )
    if options_dict["d_speaker_embedding"] is None:
        ae_record_dict = training.train_fixed_epochs_external_val(
            options_dict["ae_n_epochs"], optimizer, loss, train_batch_iterator,
            [a, a_lengths, b, b_lengths], samediff_val,
            save_model_fn=pretrain_intermediate_model_fn,
            save_best_val_model_fn=pretrain_model_fn,
            n_val_interval=options_dict["n_val_interval"]
            )
    else:
        ae_record_dict = training.train_fixed_epochs_external_val(
            options_dict["ae_n_epochs"], optimizer, loss, train_batch_iterator,
            [a, a_lengths, b, b_lengths, speaker_id], samediff_val,
            save_model_fn=pretrain_intermediate_model_fn,
            save_best_val_model_fn=pretrain_model_fn,
            n_val_interval=options_dict["n_val_interval"]
            )


    # CORRESPONDENCE TRAINING: TRAIN AND VALIDATE

    if options_dict["cae_n_epochs"] > 0:
        print("Training model")

        cae_pretrain_model_fn = pretrain_model_fn
        if options_dict["pretrain_usefinal"]:
            ae_pretrain_model_fn = pretrain_intermediate_model_fn
        if options_dict["ae_n_epochs"] == 0:
            cae_pretrain_model_fn = None

        # Train CAE
        val_model_fn = intermediate_model_fn
        train_batch_iterator = batching.PairedBucketIterator(
            train_x, pair_list, batch_size=options_dict["cae_batch_size"],
            n_buckets=options_dict["cae_n_buckets"], shuffle_every_epoch=True,
            speaker_ids=None if options_dict["d_speaker_embedding"] is None
            else train_speaker_ids
            )
        if options_dict["d_speaker_embedding"] is None:
            cae_record_dict = training.train_fixed_epochs_external_val(
                options_dict["cae_n_epochs"], optimizer, loss,
                train_batch_iterator, [a, a_lengths, b, b_lengths],
                samediff_val, save_model_fn=intermediate_model_fn,
                save_best_val_model_fn=model_fn,
                n_val_interval=options_dict["n_val_interval"],
                load_model_fn=cae_pretrain_model_fn
                )
        else:
            cae_record_dict = training.train_fixed_epochs_external_val(
                options_dict["cae_n_epochs"], optimizer, loss,
                train_batch_iterator, [a, a_lengths, b, b_lengths, speaker_id],
                samediff_val, save_model_fn=intermediate_model_fn,
                save_best_val_model_fn=model_fn,
                n_val_interval=options_dict["n_val_interval"],
                load_model_fn=cae_pretrain_model_fn
                )

    # Save record
    record_dict_fn = path.join(model_dir, "record_dict.pkl")
    print("Writing:", record_dict_fn)
    with open(record_dict_fn, "wb") as f:
        pickle.dump(ae_record_dict, f, -1)
        if options_dict["cae_n_epochs"] > 0:
            pickle.dump(cae_record_dict, f, -1)

    # Save options_dict
    options_dict_fn = path.join(model_dir, "options_dict.pkl")
    print("Writing:" + options_dict_fn)
    with open(options_dict_fn, "wb") as f:
        pickle.dump(options_dict, f, -1)


    # FINAL EXTRINSIC EVALUATION

    print ("Performing final validation")
    if options_dict["cae_n_epochs"] == 0:
        if options_dict["extrinsic_usefinal"]:
            val_model_fn = pretrain_intermediate_model_fn
        else:
            val_model_fn = pretrain_model_fn
    else:
        if options_dict["extrinsic_usefinal"]:
            val_model_fn = intermediate_model_fn
        else:
            val_model_fn = model_fn
    prb, ap = samediff_val(normalise=False)
    ap = -ap
    prb_normalised, ap_normalised = samediff_val(normalise=True)
    ap_normalised = -ap_normalised
    print("Validation AP:", ap)
    print("Validation AP with normalisation:", ap_normalised)
    ap_fn = path.join(model_dir, "val_ap.txt")
    print("Writing:", ap_fn)
    with open(ap_fn, "w") as f:
        f.write(str(ap) + "\n")
        f.write(str(ap_normalised) + "\n")
    print("Validation model:", val_model_fn)

    print(datetime.now())


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__.strip().split("\n")[0]
        )
    parser.add_argument(
        "--data_dir", type=str,
        help="load data from this directory (default: %(default)s)",
        default=default_options_dict["data_dir"]
        )
    parser.add_argument(
        "--ae_n_epochs", type=int,
        help="number of epochs of AE pre-training (default: %(default)s)",
        default=default_options_dict["ae_n_epochs"]
        )
    parser.add_argument(
        "--cae_n_epochs", type=int,
        help="number of epochs of CAE training (default: %(default)s)",
        default=default_options_dict["cae_n_epochs"]
        )
    parser.add_argument(
        "--ae_batch_size", type=int,
        help="size of mini-batch for AE pre-training (default: %(default)s)",
        default=default_options_dict["ae_batch_size"]
        )
    parser.add_argument(
        "--cae_batch_size", type=int,
        help="size of mini-batch for CAE training (default: %(default)s)",
        default=default_options_dict["cae_batch_size"]
        )
    parser.add_argument(
        "--n_hiddens", type=int,
        help="number of hidden units in both the encoder and decoder "
        "(only used if n_layers is also given)"
        )
    parser.add_argument(
        "--dec_n_layers", type=int,
        help="number of hidden layers in both the encoder and decoder "
        "(only used if n_hiddens is also given)"
        )
    parser.add_argument(
        "--enc_n_layers", type=int,
        help="number of hidden layers in both the encoder and decoder "
        "(only used if n_hiddens is also given)"
        )
    parser.add_argument(
        "--keep_prob", type=float,
        help="dropout keep probability (default: %(default)s)",
        default=default_options_dict["keep_prob"]
        )
    parser.add_argument(
        "--train_tag", type=str, choices=["gt", "gt2", "utd", "rnd"],
        help="training set tag (default: %(default)s)",
        default=default_options_dict["train_tag"]
        )
    parser.add_argument(
        "--bidirectional", action="store_true",
        help="use bidirectional encoder and decoder layers "
        "(default: %(default)s)",
        default=default_options_dict["bidirectional"]
        )
    parser.add_argument(
        "--pretrain_usefinal", action="store_true",
        help="if set, do not use best validation AE model, but rather use "
        "final model (default: %(default)s)",
        default=default_options_dict["pretrain_usefinal"]
        )
    parser.add_argument(
        "--extrinsic_usefinal", action="store_true",
        help="if set, during final extrinsic evaluation, the final saved "
        "model will be used instead of the validation best (default: "
        "%(default)s)",
        default=default_options_dict["extrinsic_usefinal"]
        )
    parser.add_argument(
        "--use_test_for_val", action="store_true",
        help="if set, use the test data for validation (cheating, so only "
        "use when doing final evaluation, otherwise this is cheating) "
        "(default: %(default)s)",
        default=default_options_dict["use_test_for_val"]
        )
    parser.add_argument(
        "--rnd_seed", type=int, help="random seed (default: %(default)s)",
        default=default_options_dict["rnd_seed"]
        )

    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()

    # Set options
    options_dict = default_options_dict.copy()
    options_dict["script"] = "train_cae"
    options_dict["data_dir"] = args.data_dir
    options_dict["ae_n_epochs"] = args.ae_n_epochs
    options_dict["cae_n_epochs"] = args.cae_n_epochs
    options_dict["keep_prob"] = args.keep_prob
    options_dict["ae_batch_size"] = args.ae_batch_size
    options_dict["cae_batch_size"] = args.cae_batch_size
    options_dict["bidirectional"] = args.bidirectional
    options_dict["pretrain_usefinal"] = args.pretrain_usefinal
    options_dict["extrinsic_usefinal"] = args.extrinsic_usefinal
    options_dict["use_test_for_val"] = args.use_test_for_val
    options_dict["train_tag"] = args.train_tag
    options_dict["rnd_seed"] = args.rnd_seed
    if args.n_hiddens is not None and args.enc_n_layers is not None:
        options_dict["enc_n_hiddens"] = [1]*args.enc_n_layers
    if args.n_hiddens is not None and args.dec_n_layers is not None:
        options_dict["dec_n_hiddens"] = [1]*args.dec_n_layers
    if args.n_hiddens is not None:
        for i in xrange(len(options_dict["enc_n_hiddens"])):
            options_dict["enc_n_hiddens"][i] = args.n_hiddens
        for i in xrange(len(options_dict["dec_n_hiddens"])):
            options_dict["dec_n_hiddens"][i] = args.n_hiddens

    # Train model
    train_cae(options_dict)


if __name__ == "__main__":
    main()
