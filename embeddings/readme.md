Acoustic Word Embedding Models and Evaluation
=============================================

Data preparation
----------------
Create links to the MFCC NumPy archives:

    ./link_buckeye_mfcc.py
    ./link_xitsonga_mfcc.py
    
For Xitsonga, only UTD segments and test data is used; all validation (i.e.
choosing hyper-parameters) is based on the Buckeye English validation data.


Correspondence autoencoder
--------------------------
Train a recurrent CAE on ground truth segments:

    # Buckeye
    ./train_cae.py --cae_n_epochs 30 --train_tag gt

Evaluate the model:

    # Validation
    ./apply_model.py \
        models/buckeye.mfcc.gt/train_cae/60a4a9619e/cae.best_val.ckpt val
    ./eval_samediff.py --mvn \
        models/buckeye.mfcc.gt/train_cae/60a4a9619e/cae.best_val.val.npz

    # Test
    ./apply_model.py \
        models/buckeye.mfcc.gt/train_cae/60a4a9619e/cae.best_val.ckpt test
    ./eval_samediff.py --mvn \
        models/buckeye.mfcc.gt/train_cae/60a4a9619e/cae.best_val.test.npz

All the models trained below (including autoencoder and VAE models) can be
evaluated using these scripts.

Analyse embeddings:

    ./analyse_embeds.py --normalise 
        --word_type \
        because,yknow,people,something,anything,education,situation \
        models/buckeye.mfcc.utd/train_cae/e6f4584e05/cae.best_val.test.npz

    ./analyse_embeds.py --normalise --word_type \
        because,basically,exactly,probably,yknow,school,sometimes,something,education,situation \
        models/buckeye.mfcc.utd/train_cae/e6f4584e05/cae.best_val.test.npz

Train a recurrent CAE on UTD segments:

    # Buckeye
    ./train_cae.py --train_tag utd

    # Xitsonga
    ./train_cae.py --data_dir data/xitsonga.mfcc --train_tag utd \
        --pretrain_usefinal --extrinsic_usefinal --use_test_for_val
        --cae_n_epochs 3

Apply a Buckeye CAE on Xitsonga:

    ./apply_model.py --language xitsonga \
        models/buckeye.mfcc.gt/train_cae/546fd9ac51/cae.best_val.ckpt test
    ./eval_samediff.py --mvn \
        models/buckeye.mfcc.gt/train_cae/546fd9ac51/cae.best_val.xitsonga.test.npz


Autoencoder
-----------
To train a recurrent AE, we actually use the same script as for the CAE, but
only with the AE pre-training step.

Train a recurrent AE on ground truth segments:

    ./train_cae.py --ae_batch_size 300 --train_tag gt2 --cae_n_epochs 0

Train a recurrent AE on random segments:

    ./train_cae.py --train_tag rnd --ae_batch_size 300 --cae_n_epochs 0

Train a recurrent AE on UTD segments:

    ./train_cae.py --train_tag utd --cae_n_epochs 0


Variational autoencoder
-----------------------
Train a recurrent VAE on ground truth segments:

    ./train_vae.py --batch_size 500 --train_tag gt2

Train a recurrent VAE on random segments:

    # Buckeye
    ./train_vae.py --batch_size 300 --train_tag rnd

Train a recurrent VAE on UTD segments:

    # Buckeye
    ./train_vae.py --batch_size 300 --train_tag utd


Siamese model
-------------
Train a Siamese model on ground segments:

    ./train_siamese.py --n_epochs 50 --train_tag gt

Evaluate the model:

    # Validation
    ./apply_model.py \
        models/buckeye.mfcc.gt/train_siamese/???/cae.best_val.ckpt val
    ./eval_samediff.py --mvn \
        models/buckeye.mfcc.gt/train_siamese/???/cae.best_val.val.npz

    # Test
    ./apply_model.py \
        models/buckeye.mfcc.gt/train_siamese/???/cae.best_val.ckpt test
    ./eval_samediff.py --mvn \
        models/buckeye.mfcc.gt/train_siamese/???/cae.best_val.test.npz


Sweeping across models
----------------------
Multiple models can be run in series and the evaluated. Here is an example of
running a model with different seeds:

    ./sweep.py --static_args "--train_tag utd" \
        --rnd_seed 1,2,3,4,5 train_cae &> models/train_cae.sweep1

The log files produced by `sweep.py` can be analysed as follows (this includes
combining the different evaluations):

    ./analyse_sweep.py models/train_cae.sweep1

Perform test-set evaluation on a sweep:

    ./test_sweep.py models/train_cae.sweep1


Results: Buckeye
----------------

### EncDec-CAE trained on ground truth segments:

Sweep:

    ./sweep.py --static_args \
        "--cae_n_epochs 30 --train_tag gt --pretrain_usefinal" \
        --rnd_seed 1,2,3,4,5 train_cae &> models/train_cae.paper.sweep12

Validation results:

    Validation AP mean: 0.3783 (+- 0.0143)
    Validation AP with normalisation mean: 0.3806 (+- 0.0137)

Test results (needs to be performed manually on each model and saved in
`test_ap.txt` in the model directory):

    Test AP mean: 0.3847 (+- 0.0118)
    Test AP with normalisation mean: 0.3915 (+- 0.0134)

### EncDec-CAE trained on UTD segments:

Sweep:

    ./sweep.py --static_args \
        "--cae_n_epochs 10 --train_tag utd --pretrain_usefinal" \
        --rnd_seed 1,2,3,4,5 train_cae &> models/train_cae.paper.sweep11

Results:

    Validation AP mean: 0.2930 (+- 0.0122)
    Validation AP with normalisation mean: 0.3184 (+- 0.0085)
    Test AP mean: 0.2732 (+- 0.0107)
    Test AP with normalisation mean: 0.3093 (+- 0.0101)

### EncDec-CAE trained without initialising from EncDec-AE:

Sweep:

    ./sweep.py --static_args \
        "--cae_n_epochs 150 --train_tag gt --ae_n_epochs 0" \
        --rnd_seed 1,2,3,4,5 train_cae &> models/train_cae.paper.sweep13
    ./sweep.py --static_args \
        "--cae_n_epochs 150 --train_tag utd --ae_n_epochs 0" \
        --rnd_seed 1,2,3,4,5 train_cae &> models/train_cae.paper.sweep14

Results (ground truth):

    Validation AP mean: 0.2078 (+- 0.0068)
    Validation AP with normalisation mean: 0.2059 (+- 0.0063)

Results (UTD):

    Validation AP mean: 0.0952 (+- 0.0075)
    Validation AP with normalisation mean: 0.1205 (+- 0.0054)

### EncDec-AE trained on ground truth segments:

Sweep:

    ./sweep.py --static_args "--train_tag gt2 --cae_n_epochs 0" \
        --rnd_seed 1,2,3,4,5 train_cae &> models/train_ae.paper.sweep3

Validation results:

    Validation AP mean: 0.2371 (+- 0.0124)
    Validation AP with normalisation mean: 0.2621 (+- 0.0029)
    Test AP mean: 0.2171 (+- 0.0126)
    Test AP with normalisation mean: 0.2459 (+- 0.0048)

### EncDec-AE trained on random segments:

Sweep:

    ./sweep.py --static_args "--train_tag rnd --cae_n_epochs 0" \
        --rnd_seed 1,2,3,4,5 train_cae &> models/train_ae.paper.sweep4

Results:

    Validation AP mean: 0.2420 (+- 0.0058)
    Validation AP with normalisation mean: 0.2549 (+- 0.0030)
    Test AP mean: 0.2291 (+- 0.0081)
    Test AP with normalisation mean: 0.2429 (+- 0.0024)

### EncDec-AE trained on UTD segments:

Sweep:

    ./sweep.py --static_args "--train_tag utd --cae_n_epochs 0" \
        --rnd_seed 1,2,3,4,5 train_cae &> models/train_ae.paper.sweep5

Results:

    Validation AP mean: 0.2397 (+- 0.0048)
    Validation AP with normalisation mean: 0.2568 (+- 0.0028)
    Test AP mean: 0.2286 (+- 0.0093)
    Test AP with normalisation mean: 0.2483 (+- 0.0046)

### EncDec-VAE trained on ground truth segments:

Sweep:

    ./sweep.py --static_args "--train_tag gt2 --n_epochs 400" \
        --rnd_seed 1,2,3,4,5 train_vae &> models/train_vae.paper.sweep10

Results:

    Validation AP mean: 0.2605 (+- 0.0033)
    Validation AP with normalisation mean: 0.2575 (+- 0.0021)

### EncDec-VAE trained on random segments:

Sweep:

    ./sweep.py --static_args "--train_tag rnd --n_epochs 400" \
        --rnd_seed 1,2,3,4,5 train_vae &> models/train_vae.paper.sweep9

Results:

    Validation AP mean: 0.2458 (+- 0.0035)
    Validation AP with normalisation mean: 0.2537 (+- 0.0056)

### EncDec-VAE trained on UTD segments:

Sweep:

    ./sweep.py --static_args "--train_tag utd --n_epochs 400" \
        --rnd_seed 1,2,3,4,5 train_vae &> models/train_vae.paper.sweep8

Results:

    Validation AP mean: 0.2520 (+- 0.0015)
    Validation AP with normalisation mean: 0.2595 (+- 0.0032)
    Test AP mean: 0.2351 (+- 0.0049)
    Test AP with normalisation mean: 0.2501 (+- 0.0024)


Results: Xitsonga
-----------------

### EncDec-CAE trained on UTD segments:

Sweep:

    ./sweep.py --static_args \
        "--data_dir data/xitsonga.mfcc --pretrain_usefinal --extrinsic_usefinal --use_test_for_val --cae_n_epochs 3 --train_tag utd" \
        --rnd_seed 1,2,3,4,5 train_cae &> models/train_cae_xitsonga.paper.sweep8

Test results:

    Test AP mean: 0.2913 (+- 0.0094)
    Test AP with normalisation mean: 0.3098 (+- 0.0079)

Although it says "validation" in the output, remember that we used the test
data as validation data during training without cheating, i.e. we always used
the final model through `--extrinsic_usefinal`. This is also true for all the
results below.

### EncDec-AE trained on UTD segments:

Sweep:

    ./sweep.py --static_args \
        "--data_dir data/xitsonga.mfcc --pretrain_usefinal --extrinsic_usefinal --use_test_for_val --train_tag utd --cae_n_epochs 0" \
        --rnd_seed 1,2,3,4,5 train_cae &> models/train_ae_xitsonga.paper.sweep9

Test results:

    Test AP mean: 0.1363 (+- 0.0047)
    Test AP with normalisation mean: 0.1415 (+- 0.0031)

### EncDec-VAE trained on UTD segments:

Sweep:

    ./sweep.py --static_args \
        "--data_dir data/xitsonga.mfcc --n_epochs 300 --extrinsic_usefinal --use_test_for_val --train_tag utd" \
        --rnd_seed 1,2,3,4,5 train_vae &> models/train_va_xitsongae.paper.sweep11

Test results:

    Test AP mean: 0.1097 (+- 0.0049)
    Test AP with normalisation mean: 0.1143 (+- 0.0040)
