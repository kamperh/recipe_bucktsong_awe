Same-Different Evaluation
=========================


Overview
--------
Performs same-different evaluation on frame-level features using dynamic time
warping (DTW) alignment.



Evaluation
----------
This needs to be run on a multi-core machine. Change the `n_cpus` variable in
`run_calcdists.sh` and `run_samediff.sh` to the number of CPUs on the machine.

Evaluate MFCCs:

    # Devpart2
    ./run_calcdists.sh \
        ../features/wordpairs/devpart2/devpart2.samediff.mfcc.cmvn_dd.npz
    ./run_samediff.sh  \
        ../features/wordpairs/devpart2/devpart2.samediff.mfcc.cmvn_dd.npz

    # ZeroSpeech
    ./run_calcdists.sh \
        ../features/wordpairs/zs/zs.samediff.mfcc.cmvn_dd.npz
    ./run_samediff.sh  \
        ../features/wordpairs/zs/zs.samediff.mfcc.cmvn_dd.npz

    # Xitsonga
    ./run_calcdists.sh \
        ../features/wordpairs/xitsonga/xitsonga.samediff.mfcc.cmvn_dd.npz
    ./run_samediff.sh  \
        ../features/wordpairs/xitsonga/xitsonga.samediff.mfcc.cmvn_dd.npz

Evaluate filterbanks:

    # Devpart2
    ./run_calcdists.sh \
        ../features/wordpairs/devpart2/devpart2.samediff.fbank.mvn.npz
    ./run_samediff.sh  \
        ../features/wordpairs/devpart2/devpart2.samediff.fbank.mvn.npz

    # Xitsonga
    ./run_calcdists.sh \
        ../features/wordpairs/xitsonga/xitsonga.samediff.fbank.mvn.npz
    ./run_samediff.sh  \
        ../features/wordpairs/xitsonga/xitsonga.samediff.fbank.mvn.npz



Results
-------
Devpart2 MFFCs:

    Average precision: 0.368128828362
    Precision-recall breakeven: 0.392424632827

Devpart2 filterbanks:

    Average precision: 0.203037757802
    Precision-recall breakeven: 0.26668384437

ZeroSpeech MFFCs:

    Average precision: 0.359030530567
    Precision-recall breakeven: 0.400375469337
    
Xitsonga MFFCs:

    Average precision: 0.281450179468
    Precision-recall breakeven: 0.344160051839

Xitsonga filterbanks:

    Average precision: 0.127098865168
    Precision-recall breakeven: 0.207577352989
