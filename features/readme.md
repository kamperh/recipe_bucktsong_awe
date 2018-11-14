Feature Extraction
==================

Overview
--------
These steps perform filterbank and MFCC feature extraction.



Filterbanks
-----------
Move to the filterbank feature extraction directory:

    cd fbank

Extract the filterbanks with mean and variance normalisation for the whole
Buckeye corpus:

    ./get_raw_htk.py buckeye
    ./get_segments_scp.py buckeye
    ./get_mvn_htk.py buckeye
    mkdir buckeye/numpy
    ../htk_to_npz.py --extension fbank \
        buckeye/mvn buckeye/numpy/buckeye.fbank.mvn.npz

Extract the filterbanks with mean and variance normalisation for the Xitsonga
corpus:

    ./get_raw_htk.py xitsonga
    ./get_segments_scp.py xitsonga
    ./get_mvn_htk.py xitsonga
    mkdir xitsonga/numpy
    ../htk_to_npz.py --extension fbank \
        xitsonga/mvn xitsonga/numpy/xitsonga.fbank.mvn.npz



Mel-frequency cepstral coefficients
-----------------------------------
Move to the MFCC feature extraction directory:

    cd mfcc

Extract the MFCCs with CMVN and deltas and delta-delta features for the whole
Buckeye corpus:

    ./get_raw_htk.py buckeye
    ./get_segments_scp.py buckeye
    ./get_cmvn_dd_htk.py buckeye
    mkdir buckeye/numpy
    ../htk_to_npz.py buckeye/cmvn_dd buckeye/numpy/buckeye.mfcc.cmvn_dd.npz

Extract the MFCCs with CMVN and deltas and delta-delta features for the
Xitsonga corpus:

    ./get_raw_htk.py xitsonga
    ./get_segments_scp.py xitsonga
    ./get_cmvn_dd_htk.py xitsonga
    mkdir xitsonga/numpy
    ../htk_to_npz.py xitsonga/cmvn_dd xitsonga/numpy/xitsonga.mfcc.cmvn_dd.npz



Subsets
-------
Move to the subset directory:

    cd subsets

Create Buckeye subsets:

    # Devpart1
    mkdir devpart1
    ./get_subset_npz.py ../mfcc/buckeye/numpy/buckeye.mfcc.cmvn_dd.npz \
        ../../data/devpart1_speakers.list devpart1/devpart1.mfcc.cmvn_dd.npz

    # Devpart2
    mkdir devpart2
    ./get_subset_npz.py ../mfcc/buckeye/numpy/buckeye.mfcc.cmvn_dd.npz \
        ../../data/devpart2_speakers.list devpart2/devpart2.mfcc.cmvn_dd.npz
    ./get_subset_npz.py ../fbank/buckeye/numpy/buckeye.fbank.mvn.npz \
        ../../data/devpart2_speakers.list devpart2/devpart2.fbank.mvn.npz

    # ZeroSpeech
    mkdir zs
    ./get_subset_npz.py ../mfcc/buckeye/numpy/buckeye.mfcc.cmvn_dd.npz \
        ../../data/zs_speakers.list zs/zs.mfcc.cmvn_dd.npz

Create Xitsonga subsets:

    # Xitsonga
    mkdir xitsonga
    ln -s ../../mfcc/xitsonga/numpy/xitsonga.mfcc.cmvn_dd.npz xitsonga/
    ln -s ../../fbank/xitsonga/numpy/xitsonga.fbank.mvn.npz xitsonga/

    # Xitsonga dev
    mkdir xitsonga_dev
    ./get_subset_npz.py ../mfcc/xitsonga/numpy/xitsonga.mfcc.cmvn_dd.npz \
        ../../data/xitsonga_dev_speakers.list \
        xitsonga_dev/xitsonga_dev.mfcc.cmvn_dd.npz

    # Xitsonga test
    mkdir xitsonga_test
    ./get_subset_npz.py ../mfcc/xitsonga/numpy/xitsonga.mfcc.cmvn_dd.npz \
        ../../data/xitsonga_test_speakers.list \
        xitsonga_test/xitsonga_test.mfcc.cmvn_dd.npz

Analyse speaker lists:

    ./analyse_buckeye_speaker_list.py ../data/devpart1_speakers.list
    ./analyse_buckeye_speaker_list.py ../data/zs_speakers.list

Analyse the lengths, means and variances in a given npz file:

    ./analyse_buckeye_npz.py zs/zs.mfcc.cmvn_dd.npz



Extract words
-------------
For evaluation and unsupervised training, ground truth and discovered words and
word pairs are extracted. Move to the word-pair directory:

    cd wordpairs

Get features for discovered words:

    # Buckeye
    mkdir buckeye
    ./strip_nonvad_from_pairs.py \
        ../mfcc/buckeye/lists/segments.list \
        ../../data/buckeye.fdlps.0.93.pairs \
        buckeye/buckeye_utd_pairs.list
    ./get_terms_from_pairs.py buckeye/buckeye_utd_pairs.list \
        buckeye/buckeye_utd_terms.list
    ./segments_from_npz.py \
        ../mfcc/buckeye/numpy/buckeye.mfcc.cmvn_dd.npz \
        buckeye/buckeye_utd_terms.list \
        buckeye/buckeye_utd_terms.mfcc.cmvn_dd.npz

    # Devpart1
    mkdir devpart1
    ./get_pairs_for_speakers.py \
        buckeye/buckeye_utd_pairs.list \
        ../../data/devpart1_speakers.list devpart1/devpart1_utd_pairs.list
    ./get_terms_from_pairs.py devpart1/devpart1_utd_pairs.list \
        devpart1/devpart1_utd_terms.list
    ./segments_from_npz.py \
        ../subsets/devpart1/devpart1.mfcc.cmvn_dd.npz \
        devpart1/devpart1_utd_terms.list \
        devpart1/devpart1_utd_terms.mfcc.cmvn_dd.npz

    # Xitsonga
    mkdir xitsonga
    ./strip_nonvad_from_pairs.py \
        ../mfcc/xitsonga/lists/segments.list \
        ../../data/zs_tsonga.fdlps.0.925.pairs.v0 \
        xitsonga/xitsonga_utd_pairs.list
    ./get_terms_from_pairs.py xitsonga/xitsonga_utd_pairs.list \
        xitsonga/xitsonga_utd_terms.list
    ./segments_from_npz.py \
        ../subsets/xitsonga/xitsonga.mfcc.cmvn_dd.npz \
        xitsonga/xitsonga_utd_terms.list \
        xitsonga/xitsonga_utd_terms.mfcc.cmvn_dd.npz

Get same-different words for the different subsets:

    ./get_samediff.py buckeye
    ./get_samediff.py xitsonga

    # Devpart1
    mkdir devpart1
    ./get_terms_for_speakers.py \
        buckeye/buckeye.samediff.list \
        ../../data/devpart1_speakers.list \
        devpart1/devpart1.samediff.list
    ./segments_from_npz.py \
        ../subsets/devpart1/devpart1.mfcc.cmvn_dd.npz \
        devpart1/devpart1.samediff.list \
        devpart1/devpart1.samediff.mfcc.cmvn_dd.npz

    # Devpart1: samediff2 (more segments)
    ./get_terms_for_speakers.py \
        buckeye/buckeye.samediff2.list \
        ../../data/devpart1_speakers.list \
        devpart1/devpart1.samediff2.list
    ./segments_from_npz.py \
        ../subsets/devpart1/devpart1.mfcc.cmvn_dd.npz \
        devpart1/devpart1.samediff2.list \
        devpart1/devpart1.samediff2.mfcc.cmvn_dd.npz

    # Devpart2
    mkdir devpart2
    ./get_terms_for_speakers.py \
        buckeye/buckeye.samediff.list \
        ../../data/devpart2_speakers.list \
        devpart2/devpart2.samediff.list
    ./segments_from_npz.py \
        ../subsets/devpart2/devpart2.mfcc.cmvn_dd.npz \
        devpart2/devpart2.samediff.list \
        devpart2/devpart2.samediff.mfcc.cmvn_dd.npz
    ./segments_from_npz.py \
        ../subsets/devpart2/devpart2.fbank.mvn.npz \
        devpart2/devpart2.samediff.list \
        devpart2/devpart2.samediff.fbank.mvn.npz

    # ZeroSpeech
    mkdir zs
    ./get_terms_for_speakers.py \
        buckeye/buckeye.samediff.list \
        ../../data/zs_speakers.list \
        zs/zs.samediff.list
    ./segments_from_npz.py \
        ../subsets/zs/zs.mfcc.cmvn_dd.npz \
        zs/zs.samediff.list \
        zs/zs.samediff.mfcc.cmvn_dd.npz

    # Xitsonga
    ./segments_from_npz.py \
        ../subsets/xitsonga/xitsonga.mfcc.cmvn_dd.npz \
        xitsonga/xitsonga.samediff.list \
        xitsonga/xitsonga.samediff.mfcc.cmvn_dd.npz
    ./segments_from_npz.py \
        ../subsets/xitsonga/xitsonga.fbank.mvn.npz \
        xitsonga/xitsonga.samediff.list \
        xitsonga/xitsonga.samediff.fbank.mvn.npz

    # Xitsonga dev
    mkdir xitsonga_dev
    ./segments_from_npz.py \
        ../subsets/xitsonga_dev/xitsonga_dev.mfcc.cmvn_dd.npz \
        xitsonga/xitsonga.samediff.list \
        xitsonga_dev/xitsonga_dev.samediff.mfcc.cmvn_dd.npz

    # Xitsonga test
    mkdir xitsonga_test
    ./segments_from_npz.py \
        ../subsets/xitsonga_test/xitsonga_test.mfcc.cmvn_dd.npz \
        xitsonga/xitsonga.samediff.list \
        xitsonga_test/xitsonga_test.samediff.mfcc.cmvn_dd.npz


Buckeye set definitions
-----------------------
Buckeye is divided into a number of sets based on the speakers:

- sample: s2801a, s2801b, s2802a, s2802b, s2803a, s3701a, s3701b, s3702a,
  s3702b, s3703a, s3703b
- devpart1: s02, s04, s05, s08, s12, s16, s03, s06, s10, s11, s13, s38
- devpart2: s18, s17, s37, s39, s19, s22, s40, s34
- ZS: s20, s25, s27, s01, s26, s31, s29, s23, s24, s32, s33, s30
- testpart2: s07, s14, s09, s21, s36, s35, s15, s28
- dev: devpart1 + devpart2
- test: ZS + testpart2 
