#!/usr/bin/env python

"""
Create links to the MFCC files.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2018
"""

from __future__ import division
from __future__ import print_function
from os import path
import numpy as np
import os

relative_features_dir = path.join("..", "..", "..", "features")
output_dir = path.join("data", "buckeye.mfcc")


def main():

    # Create output directory
    if not path.isdir(output_dir):
        os.makedirs(output_dir)

    # Training: All complete utterances
    npz_fn = path.join(
        relative_features_dir, "subsets", "devpart1",
        "devpart1.mfcc.cmvn_dd.npz"
        )
    link_fn = path.join(output_dir, "train.all.npz")
    if not path.isfile(link_fn):
        print("Linking:", npz_fn, "to", link_fn)
        os.symlink(npz_fn, link_fn)

    # Training: Ground truth words
    npz_fn = path.join(
        relative_features_dir, "wordpairs", "devpart1",
        "devpart1.samediff.mfcc.cmvn_dd.npz"
        )
    link_fn = path.join(output_dir, "train.gt.npz")
    if not path.isfile(link_fn):
        print("Linking:", npz_fn, "to", link_fn)
        os.symlink(npz_fn, link_fn)

    # Training: Ground truth words (more segments)
    npz_fn = path.join(
        relative_features_dir, "wordpairs", "devpart1",
        "devpart1.samediff2.mfcc.cmvn_dd.npz"
        )
    link_fn = path.join(output_dir, "train.gt2.npz")
    if not path.isfile(link_fn):
        print("Linking:", npz_fn, "to", link_fn)
        os.symlink(npz_fn, link_fn)

    # Training: UTD discovered words
    npz_fn = path.join(
        relative_features_dir, "wordpairs", "devpart1",
        "devpart1_utd_terms.mfcc.cmvn_dd.npz"
        )
    link_fn = path.join(output_dir, "train.utd.npz")
    if not path.isfile(link_fn):
        print("Linking:", npz_fn, "to", link_fn)
        os.symlink(npz_fn, link_fn)

    # Validation
    npz_fn = path.join(
        relative_features_dir, "wordpairs", "devpart2",
        "devpart2.samediff.mfcc.cmvn_dd.npz"
        )
    link_fn = path.join(output_dir, "val.npz")
    if not path.isfile(link_fn):
        print("Linking:", npz_fn, "to", link_fn)
        os.symlink(npz_fn, link_fn)

    # Test
    npz_fn = path.join(
        relative_features_dir, "wordpairs", "zs",
        "zs.samediff.mfcc.cmvn_dd.npz"
        )
    link_fn = path.join(output_dir, "test.npz")
    if not path.isfile(link_fn):
        print("Linking:", npz_fn, "to", link_fn)
        os.symlink(npz_fn, link_fn)


if __name__ == "__main__":
    main()
