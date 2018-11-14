#!/usr/bin/env python

"""
Plot t-SNE embeddings of two models.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2017, 2018
"""

from __future__ import division
from __future__ import print_function
from collections import Counter
from os import path
from sklearn import manifold
import cPickle as pickle
import matplotlib.pyplot as plt
import numpy as np
import random
import sys

# sys.path.append(path.join("..", "src"))

import plotting

KEYWORDS_FILTER = [
    "because", "basically", "exactly", "probably", "columbus", "school",
    "sometimes", "something", "education", "situation"
    ]
N_MAX_KEYWORDS = 50
TSNE_PERPLEXITY = 20


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def get_embeds_and_labels(embeds_dict, types=None):
    embeddings = []
    labels = []
    for utt in embeds_dict:
        if "_" in utt:
            label = utt.split("_")[0]
        else:
            label = utt
        if types is None:
            labels.append(label)
            embeddings.append(embeds_dict[utt])
        elif label in types:
            labels.append(label)
            embeddings.append(embeds_dict[utt])
    embeddings = np.array(embeddings)
    return embeddings, labels


def plot_labelled_2d_data(X, labels):
    classes = set(labels)
    for label in sorted(classes):
        indices = np.where(np.array(labels) == label)[0]
        plt.scatter(X[indices, 0], X[indices, 1], label=label)


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():

    npz_fn = (
        "../embeddings/models/buckeye.mfcc.utd/train_cae/e6f4584e05/"
        "cae.best_val.test.npz"
        )
    print("Reading:", npz_fn)
    npz = np.load(npz_fn)


    if True:
        print("Normalising embeddings")
        norm_npz = {}
        for key in npz:
            embed = npz[key]
            norm_npz[key] = embed/np.linalg.norm(embed)
        npz = norm_npz

    embeddings, labels = get_embeds_and_labels(norm_npz, KEYWORDS_FILTER)

    # Perform t-SNE
    tsne = manifold.TSNE(
        n_components=2, perplexity=TSNE_PERPLEXITY, init="random",
        random_state=0
        )
    X_tsne = tsne.fit_transform(embeddings)

    # Plot t-SNE
    plotting.setup_plot()
    plt.rcParams["figure.figsize"]          = 4.0, 2.5
    plt.rcParams["figure.subplot.bottom"]   = 0.01
    plt.rcParams["figure.subplot.left"]     = 0.01
    plt.rcParams["figure.subplot.right"]    = 0.99
    plt.rcParams["figure.subplot.top"]      = 0.99
    # plt.figure()
    plot_labelled_2d_data(X_tsne, labels)
    plt.legend(loc="best", ncol=2)
    # plt.xlim([-31, 34])
    plt.ylim([-21, 39])
    plt.yticks([])
    plt.xticks([])
    plt.savefig("cae_embeddings.pdf")


if __name__ == "__main__":
    main()

