Intermediate Results
====================

train_cae.sweep1
----------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 10, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'utd', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': False}
    Validation AP (rnd_seed=1): 0.2924
    Validation AP with normalisation: 0.3012
    Validation AP (rnd_seed=2): 0.2484
    Validation AP with normalisation: 0.2939
    Validation AP (rnd_seed=3): 0.2747
    Validation AP with normalisation: 0.2999
    Validation AP (rnd_seed=4): 0.2999
    Validation AP with normalisation: 0.3211
    Validation AP (rnd_seed=5): 0.3060
    Validation AP with normalisation: 0.3128
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2843 (+- 0.0208)
    Validation AP with normalisation mean: 0.3058 (+- 0.0098)
    -------------------------------------------------------------------------------



train_cae.sweep2
----------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 50, 'cae_n_epochs': 30, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'utd', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': True}
    Validation AP (rnd_seed=1): 0.2795
    Validation AP with normalisation: 0.3056
    Validation AP (rnd_seed=2): 0.2725
    Validation AP with normalisation: 0.3044
    Validation AP (rnd_seed=3): 0.2802
    Validation AP with normalisation: 0.3078
    Validation AP (rnd_seed=4): 0.2837
    Validation AP with normalisation: 0.2846
    Validation AP (rnd_seed=5): 0.2978
    Validation AP with normalisation: 0.3092
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2828 (+- 0.0084)
    Validation AP with normalisation mean: 0.3023 (+- 0.0090)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 30, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'utd', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': True}
    Validation AP (rnd_seed=1): 0.2987
    Validation AP with normalisation: 0.3168
    Validation AP (rnd_seed=2): 0.2715
    Validation AP with normalisation: 0.3065
    Validation AP (rnd_seed=3): 0.2756
    Validation AP with normalisation: 0.2958
    Validation AP (rnd_seed=4): 0.3018
    Validation AP with normalisation: 0.3233
    Validation AP (rnd_seed=5): 0.3140
    Validation AP with normalisation: 0.3249
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2923 (+- 0.0162)
    Validation AP with normalisation mean: 0.3134 (+- 0.0109)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 150, 'cae_n_epochs': 30, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'utd', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': True}
    Validation AP (rnd_seed=1): 0.3084
    Validation AP with normalisation: 0.3073
    Validation AP (rnd_seed=2): 0.2827
    Validation AP with normalisation: 0.2984
    Validation AP (rnd_seed=3): 0.3045
    Validation AP with normalisation: 0.3217
    Validation AP (rnd_seed=4): 0.2999
    Validation AP with normalisation: 0.3136
    Validation AP (rnd_seed=5): 0.3137
    Validation AP with normalisation: 0.3217
    -------------------------------------------------------------------------------
    Validation AP mean: 0.3019 (+- 0.0106)
    Validation AP with normalisation mean: 0.3125 (+- 0.0089)
    -------------------------------------------------------------------------------



train_cae.sweep3
----------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 200, 'cae_n_epochs': 10, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'utd', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': True}
    Validation AP (rnd_seed=1): 0.2820
    Validation AP with normalisation: 0.3170
    Validation AP (rnd_seed=2): 0.2870
    Validation AP with normalisation: 0.3169
    Validation AP (rnd_seed=3): 0.2824
    Validation AP with normalisation: 0.3121
    Validation AP (rnd_seed=4): 0.2989
    Validation AP with normalisation: 0.3248
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2876 (+- 0.0068)
    Validation AP with normalisation mean: 0.3177 (+- 0.0045)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 400, 'cae_n_epochs': 10, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'utd', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': True}
    Validation AP (rnd_seed=1): 0.2707
    Validation AP with normalisation: 0.3159
    Validation AP (rnd_seed=2): 0.2944
    Validation AP with normalisation: 0.3094
    Validation AP (rnd_seed=3): 0.2763
    Validation AP with normalisation: 0.3051
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2805 (+- 0.0101)
    Validation AP with normalisation mean: 0.3101 (+- 0.0044)
    -------------------------------------------------------------------------------



models/train_cae.sweep4
-----------------------
    
    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 10, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'utd', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': True}
    Validation AP (rnd_seed=1): 0.2960
    Validation AP with normalisation: 0.3204
    Validation AP (rnd_seed=2): 0.2594
    Validation AP with normalisation: 0.2983
    Validation AP (rnd_seed=3): 0.2903
    Validation AP with normalisation: 0.3159
    Validation AP (rnd_seed=4): 0.2954
    Validation AP with normalisation: 0.3182
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2853 (+- 0.0151)
    Validation AP with normalisation mean: 0.3132 (+- 0.0088)
    -------------------------------------------------------------------------------



models/train_cae.sweep5
-----------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 10, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'utd', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': False}
    Validation AP (rnd_seed=1): 0.2882
    Validation AP with normalisation: 0.3250
    Validation AP (rnd_seed=2): 0.2837
    Validation AP with normalisation: 0.3159
    Validation AP (rnd_seed=3): 0.2902
    Validation AP with normalisation: 0.3227
    Validation AP (rnd_seed=4): 0.2920
    Validation AP with normalisation: 0.3091
    Validation AP (rnd_seed=5): 0.3261
    Validation AP with normalisation: 0.3355
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2960 (+- 0.0153)
    Validation AP with normalisation mean: 0.3217 (+- 0.0089)
    -------------------------------------------------------------------------------



models/train_cae.sweep6
-----------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 10, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'utd', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [100, 100, 100], 'bidirectional': True, 'dec_n_hiddens': [100, 100, 100], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': False}
    Validation AP (rnd_seed=1): 0.2386
    Validation AP with normalisation: 0.2841
    Validation AP (rnd_seed=2): 0.2059
    Validation AP with normalisation: 0.2521
    Validation AP (rnd_seed=3): 0.2325
    Validation AP with normalisation: 0.2657
    Validation AP (rnd_seed=4): 0.2480
    Validation AP with normalisation: 0.2643
    Validation AP (rnd_seed=5): 0.2386
    Validation AP with normalisation: 0.2680
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2327 (+- 0.0143)
    Validation AP with normalisation mean: 0.2668 (+- 0.0103)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 10, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'utd', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [200, 200, 200], 'bidirectional': True, 'dec_n_hiddens': [200, 200, 200], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': False}
    Validation AP (rnd_seed=1): 0.2355
    Validation AP with normalisation: 0.2681
    Validation AP (rnd_seed=2): 0.2344
    Validation AP with normalisation: 0.2824
    Validation AP (rnd_seed=3): 0.2530
    Validation AP with normalisation: 0.2889
    Validation AP (rnd_seed=4): 0.2631
    Validation AP with normalisation: 0.2954
    Validation AP (rnd_seed=5): 0.2202
    Validation AP with normalisation: 0.2735
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2412 (+- 0.0151)
    Validation AP with normalisation mean: 0.2817 (+- 0.0099)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 10, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'utd', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': True, 'dec_n_hiddens': [400, 400, 400], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': False}
    Validation AP (rnd_seed=1): 0.2355
    Validation AP with normalisation: 0.2807
    Validation AP (rnd_seed=2): 0.2611
    Validation AP with normalisation: 0.2942
    Validation AP (rnd_seed=3): 0.2440
    Validation AP with normalisation: 0.2961
    Validation AP (rnd_seed=4): 0.2609
    Validation AP with normalisation: 0.2914
    Validation AP (rnd_seed=5): 0.2415
    Validation AP with normalisation: 0.2910
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2486 (+- 0.0105)
    Validation AP with normalisation mean: 0.2907 (+- 0.0053)
    -------------------------------------------------------------------------------



models/train_cae.sweep7
-----------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 0, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'gt', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 200, 'pretrain_usefinal': False}
    Validation AP (rnd_seed=1): 0.2544
    Validation AP with normalisation: 0.2591
    Validation AP (rnd_seed=2): 0.2516
    Validation AP with normalisation: 0.2570
    Validation AP (rnd_seed=3): 0.2562
    Validation AP with normalisation: 0.2591
    Validation AP (rnd_seed=4): 0.2536
    Validation AP with normalisation: 0.2593
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2539 (+- 0.0017)
    Validation AP with normalisation mean: 0.2586 (+- 0.0009)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 0, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'gt2', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 200, 'pretrain_usefinal': False}
    Validation AP (rnd_seed=1): 0.2533
    Validation AP with normalisation: 0.2617
    Validation AP (rnd_seed=2): 0.2426
    Validation AP with normalisation: 0.2550
    Validation AP (rnd_seed=3): 0.2119
    Validation AP with normalisation: 0.2506
    Validation AP (rnd_seed=4): 0.2234
    Validation AP with normalisation: 0.2522
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2328 (+- 0.0161)
    Validation AP with normalisation mean: 0.2549 (+- 0.0042)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 0, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'gt', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': False}
    Validation AP (rnd_seed=1): 0.2215
    Validation AP with normalisation: 0.2281
    Validation AP (rnd_seed=2): 0.2343
    Validation AP with normalisation: 0.2377
    Validation AP (rnd_seed=3): 0.2275
    Validation AP with normalisation: 0.2317
    Validation AP (rnd_seed=4): 0.2277
    Validation AP with normalisation: 0.2296
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2278 (+- 0.0045)
    Validation AP with normalisation mean: 0.2318 (+- 0.0037)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 0, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'gt2', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 300, 'pretrain_usefinal': False}
    Validation AP (rnd_seed=1): 0.2524
    Validation AP with normalisation: 0.2649
    Validation AP (rnd_seed=2): 0.2333
    Validation AP with normalisation: 0.2598
    Validation AP (rnd_seed=3): 0.2299
    Validation AP with normalisation: 0.2592
    Validation AP (rnd_seed=4): 0.2484
    Validation AP with normalisation: 0.2627
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2410 (+- 0.0096)
    Validation AP with normalisation mean: 0.2616 (+- 0.0023)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 0, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'gt', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 500, 'pretrain_usefinal': False}
    Validation AP (rnd_seed=1): 0.2060
    Validation AP with normalisation: 0.2095
    Validation AP (rnd_seed=2): 0.2223
    Validation AP with normalisation: 0.2267
    Validation AP (rnd_seed=3): 0.2212
    Validation AP with normalisation: 0.2274
    Validation AP (rnd_seed=4): 0.2073
    Validation AP with normalisation: 0.2126
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2142 (+- 0.0076)
    Validation AP with normalisation mean: 0.2190 (+- 0.0081)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'rnn_type': 'gru', 'cae_batch_size': 300, 'n_z': 130, 'keep_prob': 1.0, 'ae_n_epochs': 100, 'cae_n_epochs': 0, 'data_dir': 'data/buckeye.mfcc', 'script': 'train_cae', 'cae_n_buckets': 3, 'n_input': 13, 'max_length': 100, 'train_tag': 'gt2', 'ae_n_buckets': 3, 'learning_rate': 0.001, 'enc_n_hiddens': [400, 400, 400], 'bidirectional': False, 'dec_n_hiddens': [400, 400, 400], 'min_length': 50, 'use_test_for_val': False, 'n_val_interval': 1, 'extrinsic_usefinal': False, 'ae_batch_size': 500, 'pretrain_usefinal': False}
    Validation AP (rnd_seed=1): 0.2465
    Validation AP with normalisation: 0.2508
    Validation AP (rnd_seed=2): 0.2283
    Validation AP with normalisation: 0.2308
    Validation AP (rnd_seed=3): 0.2535
    Validation AP with normalisation: 0.2591
    Validation AP (rnd_seed=4): 0.2463
    Validation AP with normalisation: 0.2575
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2436 (+- 0.0093)
    Validation AP with normalisation mean: 0.2496 (+- 0.0113)
    -------------------------------------------------------------------------------



train_vae.sweep1
----------------

    -------------------------------------------------------------------------------
    {'min_length': 50, 'use_test_for_val': False, 'n_z': 130, 'script': 'train_vae', 'learning_rate': 0.001, 'batch_size': 200, 'n_epochs': 100, 'n_val_interval': 1, 'max_length': 100, 'enc_n_hiddens': [400, 400, 400], 'train_tag': 'rnd', 'n_buckets': 3, 'bidirectional': False, 'data_dir': 'data/buckeye.mfcc', 'n_input': 13, 'extrinsic_usefinal': False, 'dec_n_hiddens': [400, 400, 400], 'rnn_type': 'gru', 'keep_prob': 1.0, 'sigma_sq': 1e-05}
    Validation AP (rnd_seed=1): 0.2476
    Validation AP with normalisation: 0.2486
    Validation AP (rnd_seed=2): 0.2411
    Validation AP with normalisation: 0.2476
    Validation AP (rnd_seed=3): 0.2336
    Validation AP with normalisation: 0.2432
    Validation AP (rnd_seed=4): 0.2507
    Validation AP with normalisation: 0.2530
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2433 (+- 0.0066)
    Validation AP with normalisation mean: 0.2481 (+- 0.0035)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'min_length': 50, 'use_test_for_val': False, 'n_z': 130, 'script': 'train_vae', 'learning_rate': 0.001, 'batch_size': 200, 'n_epochs': 100, 'n_val_interval': 1, 'max_length': 100, 'enc_n_hiddens': [400, 400, 400], 'train_tag': 'utd', 'n_buckets': 3, 'bidirectional': False, 'data_dir': 'data/buckeye.mfcc', 'n_input': 13, 'extrinsic_usefinal': False, 'dec_n_hiddens': [400, 400, 400], 'rnn_type': 'gru', 'keep_prob': 1.0, 'sigma_sq': 1e-05}
    Validation AP (rnd_seed=1): 0.2416
    Validation AP with normalisation: 0.2569
    Validation AP (rnd_seed=2): 0.2527
    Validation AP with normalisation: 0.2578
    Validation AP (rnd_seed=3): 0.2451
    Validation AP with normalisation: 0.2595
    Validation AP (rnd_seed=4): 0.2375
    Validation AP with normalisation: 0.2555
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2442 (+- 0.0056)
    Validation AP with normalisation mean: 0.2574 (+- 0.0014)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'min_length': 50, 'use_test_for_val': False, 'n_z': 130, 'script': 'train_vae', 'learning_rate': 0.001, 'batch_size': 300, 'n_epochs': 100, 'n_val_interval': 1, 'max_length': 100, 'enc_n_hiddens': [400, 400, 400], 'train_tag': 'rnd', 'n_buckets': 3, 'bidirectional': False, 'data_dir': 'data/buckeye.mfcc', 'n_input': 13, 'extrinsic_usefinal': False, 'dec_n_hiddens': [400, 400, 400], 'rnn_type': 'gru', 'keep_prob': 1.0, 'sigma_sq': 1e-05}
    Validation AP (rnd_seed=1): 0.2516
    Validation AP with normalisation: 0.2559
    Validation AP (rnd_seed=2): 0.2470
    Validation AP with normalisation: 0.2534
    Validation AP (rnd_seed=3): 0.2515
    Validation AP with normalisation: 0.2570
    Validation AP (rnd_seed=4): 0.2483
    Validation AP with normalisation: 0.2551
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2496 (+- 0.0020)
    Validation AP with normalisation mean: 0.2554 (+- 0.0013)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'min_length': 50, 'use_test_for_val': False, 'n_z': 130, 'script': 'train_vae', 'learning_rate': 0.001, 'batch_size': 300, 'n_epochs': 100, 'n_val_interval': 1, 'max_length': 100, 'enc_n_hiddens': [400, 400, 400], 'train_tag': 'utd', 'n_buckets': 3, 'bidirectional': False, 'data_dir': 'data/buckeye.mfcc', 'n_input': 13, 'extrinsic_usefinal': False, 'dec_n_hiddens': [400, 400, 400], 'rnn_type': 'gru', 'keep_prob': 1.0, 'sigma_sq': 1e-05}
    Validation AP (rnd_seed=1): 0.2546
    Validation AP with normalisation: 0.2595
    Validation AP (rnd_seed=2): 0.2486
    Validation AP with normalisation: 0.2609
    Validation AP (rnd_seed=3): 0.2628
    Validation AP with normalisation: 0.2689
    Validation AP (rnd_seed=4): 0.2524
    Validation AP with normalisation: 0.2654
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2546 (+- 0.0052)
    Validation AP with normalisation mean: 0.2636 (+- 0.0037)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'min_length': 50, 'use_test_for_val': False, 'n_z': 130, 'script': 'train_vae', 'learning_rate': 0.001, 'batch_size': 500, 'n_epochs': 100, 'n_val_interval': 1, 'max_length': 100, 'enc_n_hiddens': [400, 400, 400], 'train_tag': 'rnd', 'n_buckets': 3, 'bidirectional': False, 'data_dir': 'data/buckeye.mfcc', 'n_input': 13, 'extrinsic_usefinal': False, 'dec_n_hiddens': [400, 400, 400], 'rnn_type': 'gru', 'keep_prob': 1.0, 'sigma_sq': 1e-05}
    Validation AP (rnd_seed=1): 0.2403
    Validation AP with normalisation: 0.2459
    Validation AP (rnd_seed=2): 0.2239
    Validation AP with normalisation: 0.2355
    Validation AP (rnd_seed=3): 0.2452
    Validation AP with normalisation: 0.2503
    Validation AP (rnd_seed=4): 0.2490
    Validation AP with normalisation: 0.2572
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2396 (+- 0.0096)
    Validation AP with normalisation mean: 0.2472 (+- 0.0079)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'min_length': 50, 'use_test_for_val': False, 'n_z': 130, 'script': 'train_vae', 'learning_rate': 0.001, 'batch_size': 500, 'n_epochs': 100, 'n_val_interval': 1, 'max_length': 100, 'enc_n_hiddens': [400, 400, 400], 'train_tag': 'utd', 'n_buckets': 3, 'bidirectional': False, 'data_dir': 'data/buckeye.mfcc', 'n_input': 13, 'extrinsic_usefinal': False, 'dec_n_hiddens': [400, 400, 400], 'rnn_type': 'gru', 'keep_prob': 1.0, 'sigma_sq': 1e-05}
    Validation AP (rnd_seed=1): 0.2449
    Validation AP with normalisation: 0.2592
    Validation AP (rnd_seed=2): 0.2443
    Validation AP with normalisation: 0.2589
    Validation AP (rnd_seed=3): 0.2486
    Validation AP with normalisation: 0.2573
    Validation AP (rnd_seed=4): 0.2405
    Validation AP with normalisation: 0.2616
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2446 (+- 0.0029)
    Validation AP with normalisation mean: 0.2593 (+- 0.0015)
    -------------------------------------------------------------------------------


train_vae.sweep2
----------------

    -------------------------------------------------------------------------------
    {'min_length': 50, 'use_test_for_val': False, 'n_z': 130, 'script': 'train_vae', 'learning_rate': 0.001, 'batch_size': 500, 'n_epochs': 200, 'n_val_interval': 1, 'max_length': 100, 'enc_n_hiddens': [400, 400, 400], 'train_tag': 'utd', 'n_buckets': 3, 'bidirectional': False, 'data_dir': 'data/buckeye.mfcc', 'n_input': 13, 'extrinsic_usefinal': False, 'dec_n_hiddens': [400, 400, 400], 'rnn_type': 'gru', 'keep_prob': 1.0, 'sigma_sq': 5e-06}
    Validation AP (rnd_seed=1): 0.2532
    Validation AP with normalisation: 0.2619
    Validation AP (rnd_seed=2): 0.2462
    Validation AP with normalisation: 0.2555
    Validation AP (rnd_seed=3): 0.2443
    Validation AP with normalisation: 0.2520
    Validation AP (rnd_seed=4): 0.2456
    Validation AP with normalisation: 0.2592
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2473 (+- 0.0035)
    Validation AP with normalisation mean: 0.2572 (+- 0.0037)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'min_length': 50, 'use_test_for_val': False, 'n_z': 130, 'script': 'train_vae', 'learning_rate': 0.001, 'batch_size': 500, 'n_epochs': 200, 'n_val_interval': 1, 'max_length': 100, 'enc_n_hiddens': [400, 400, 400], 'train_tag': 'utd', 'n_buckets': 3, 'bidirectional': False, 'data_dir': 'data/buckeye.mfcc', 'n_input': 13, 'extrinsic_usefinal': False, 'dec_n_hiddens': [400, 400, 400], 'rnn_type': 'gru', 'keep_prob': 1.0, 'sigma_sq': 1e-05}
    Validation AP (rnd_seed=1): 0.2503
    Validation AP with normalisation: 0.2629
    Validation AP (rnd_seed=2): 0.2536
    Validation AP with normalisation: 0.2629
    Validation AP (rnd_seed=3): 0.2519
    Validation AP with normalisation: 0.2581
    Validation AP (rnd_seed=4): 0.2497
    Validation AP with normalisation: 0.2615
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2514 (+- 0.0015)
    Validation AP with normalisation mean: 0.2614 (+- 0.0020)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'min_length': 50, 'use_test_for_val': False, 'n_z': 130, 'script': 'train_vae', 'learning_rate': 0.001, 'batch_size': 500, 'n_epochs': 200, 'n_val_interval': 1, 'max_length': 100, 'enc_n_hiddens': [400, 400, 400], 'train_tag': 'utd', 'n_buckets': 3, 'bidirectional': False, 'data_dir': 'data/buckeye.mfcc', 'n_input': 13, 'extrinsic_usefinal': False, 'dec_n_hiddens': [400, 400, 400], 'rnn_type': 'gru', 'keep_prob': 1.0, 'sigma_sq': 2e-05}
    Validation AP (rnd_seed=1): 0.2460
    Validation AP with normalisation: 0.2556
    Validation AP (rnd_seed=2): 0.2532
    Validation AP with normalisation: 0.2595
    Validation AP (rnd_seed=3): 0.2532
    Validation AP with normalisation: 0.2601
    Validation AP (rnd_seed=4): 0.2472
    Validation AP with normalisation: 0.2603
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2499 (+- 0.0033)
    Validation AP with normalisation mean: 0.2589 (+- 0.0019)
    -------------------------------------------------------------------------------

    -------------------------------------------------------------------------------
    {'min_length': 50, 'use_test_for_val': False, 'n_z': 130, 'script': 'train_vae', 'learning_rate': 0.001, 'batch_size': 500, 'n_epochs': 200, 'n_val_interval': 1, 'max_length': 100, 'enc_n_hiddens': [400, 400, 400], 'train_tag': 'utd', 'n_buckets': 3, 'bidirectional': False, 'data_dir': 'data/buckeye.mfcc', 'n_input': 13, 'extrinsic_usefinal': False, 'dec_n_hiddens': [400, 400, 400], 'rnn_type': 'gru', 'keep_prob': 1.0, 'sigma_sq': 0.0001}
    Validation AP (rnd_seed=1): 0.2364
    Validation AP with normalisation: 0.2358
    Validation AP (rnd_seed=2): 0.2374
    Validation AP with normalisation: 0.2334
    Validation AP (rnd_seed=3): 0.2385
    Validation AP with normalisation: 0.2232
    Validation AP (rnd_seed=4): 0.2340
    Validation AP with normalisation: 0.2216
    -------------------------------------------------------------------------------
    Validation AP mean: 0.2366 (+- 0.0017)
    Validation AP with normalisation mean: 0.2285 (+- 0.0062)
    -------------------------------------------------------------------------------
