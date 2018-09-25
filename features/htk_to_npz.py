#!/usr/bin/env python

"""
Convert all the HTK features in a given directory to a NumPy .npz format.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2015, 2018
"""

from __future__ import division
from __future__ import print_function
from os import path
import argparse
import datetime
import numpy as np
import subprocess
import sys
import glob

sys.path.append(path.join(path.dirname(__file__), "..", "src", "utils"))

from utils import shell


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__.strip().split("\n")[0], add_help=False
        )
    parser.add_argument(
        "htk_dir", type=str, help="directory with the HTK features"
        )
    parser.add_argument("npz_fn", help="NumPy output file")
    parser.add_argument(
        "--extension", type=str,
        help="the extension of the feature files (default: %(default)s)",
        default="mfcc"
        )
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()

    print(datetime.datetime.now())

    print("Reading HTK features from directory:", args.htk_dir)
    npz_dict = {}
    n_feat_files = 0
    for feat_fn in glob.glob(path.join(args.htk_dir, "*." + args.extension)):
        hlist_output = shell("HList -r " + feat_fn)
        features = [
            [float(i) for i in line.split(" ") if i != ""] for line in
            hlist_output.split("\n") if line != ""
            ]
        key = path.splitext(path.split(feat_fn)[-1])[0]
        npz_dict[key] = np.array(features)
        n_feat_files += 1
    print("Read", n_feat_files, "feature files")

    print("Writing NumPy archive:", args.npz_fn)
    np.savez(args.npz_fn, **npz_dict)

    print(datetime.datetime.now())


if __name__ == "__main__":
    main()
