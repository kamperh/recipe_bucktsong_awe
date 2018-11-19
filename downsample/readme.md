Downsampled Acoustic Word Embeddings
====================================


Overview
--------
MFCCs are downsampled to obtain acoustic word embeddings. These are evaluated
using same-different evaluation.


Downsampling
------------
Perform downsampling on MFCCs without deltas:

    # Devpart2
    n_samples=10
    mkdir -p exp/devpart2
    ./downsample.py --technique resample --frame_dims 13 \
        ../features/wordpairs/devpart2/devpart2.samediff.mfcc.cmvn_dd.npz \
        exp/devpart2/samediff.mfcc.cmvn_dd.downsample_${n_samples}.npz \
        ${n_samples}

    # ZeroSpeech
    n_samples=10
    mkdir -p exp/zs
    ./downsample.py --technique resample --frame_dims 13 \
        ../features/wordpairs/zs/zs.samediff.mfcc.cmvn_dd.npz \
        exp/zs/samediff.mfcc.cmvn_dd.downsample_${n_samples}.npz \
        ${n_samples}

    # Xitsonga
    n_samples=10
    mkdir -p exp/xitsonga
    ./downsample.py --technique resample --frame_dims 13 \
        ../features/wordpairs/xitsonga/xitsonga.samediff.mfcc.cmvn_dd.npz \
        exp/xitsonga/samediff.mfcc.cmvn_dd.downsample_${n_samples}.npz \
        ${n_samples}


Evaluation
----------
Evaluate and analyse downsampled MFCCs without deltas:

    # Devpart2
    n_samples=10
    ./eval_samediff.py --mvn \
        exp/devpart2/samediff.mfcc.cmvn_dd.downsample_${n_samples}.npz
    ./analyse_embeds.py --normalize --word_type \
        because,yknow,people,something,anything,education,situation \
        exp/devpart2/samediff.mfcc.cmvn_dd.downsample_${n_samples}.npz

    # ZeroSpeech
    n_samples=10
    ./eval_samediff.py --mvn \
        exp/zs/samediff.mfcc.cmvn_dd.downsample_${n_samples}.npz
    ./analyse_embeds.py --normalize --word_type \
        because,yknow,people,something,anything,education,situation \
        exp/zs/samediff.mfcc.cmvn_dd.downsample_${n_samples}.npz

    # Xitsonga
    n_samples=10
    ./eval_samediff.py --mvn \
        exp/xitsonga/samediff.mfcc.cmvn_dd.downsample_${n_samples}.npz
    ./analyse_embeds.py --normalize --word_type \
        kombisa,swilaveko,kahle,swinene,xiyimo,fanele,naswona,xikombelo \
        exp/xitsonga/samediff.mfcc.cmvn_dd.downsample_${n_samples}.npz


Results
-------
Devpart2 downsampled MFCCs without deltas (dimensionality=130):

    Average precision: 0.24548389092135153
    Precision-recall breakeven: 0.29062581556784084

ZeroSpeech downsampled MFCCs without deltas + mvn (dimensionality=130):

    Average precision: 0.21709397615831585
    Precision-recall breakeven: 0.27647058823529413

Xitsonga downsampled MFCCs without deltas (dimensionality=130):

    Average precision: 0.1355318866520455
    Precision-recall breakeven: 0.21024815480696055
