#!/usr/bin/env python

"""
Code the data to raw MFCCs without any normalization.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2011-2015, 2018
"""

from __future__ import division
from __future__ import print_function
from os import path
import argparse
import glob
import os
import subprocess
import sys

sys.path.append(path.join(".."))
sys.path.append(path.join("..", ".."))

from paths import buckeye_dir, xitsonga_dir
from utils import shell

config_fn = path.join("config", "hcopy.wav.fbank.wb.conf")


#-----------------------------------------------------------------------------#
#                              UTILITY FUNCTIONS                              #
#-----------------------------------------------------------------------------#

def check_argv():
    """Check the command line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__.strip().split("\n")[0], add_help=False
        )
    parser.add_argument("dataset", type=str, choices=["buckeye", "xitsonga"])
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


#-----------------------------------------------------------------------------#
#                                MAIN FUNCTION                                #
#-----------------------------------------------------------------------------#

def main():
    args = check_argv()

    if args.dataset == "buckeye":
        wavs = path.join(buckeye_dir, "*", "*.wav")
    elif args.dataset == "xitsonga":
        wavs = path.join(xitsonga_dir, "*.wav")

    target_dir = path.join(args.dataset, "raw")
    scp_dir = path.join(args.dataset, "scp")
    log_dir = path.join(args.dataset, "log")

    for d in [target_dir, scp_dir, log_dir]:
        if not path.isdir(d):
            os.makedirs(d)
    target_dir = path.abspath(target_dir)

    raw_scp = path.join(scp_dir, args.dataset + ".fbank.raw.scp")
    print("Writing raw coding SCP:", raw_scp)
    f = open(raw_scp, "w")
    for wav_fn in sorted(glob.glob(wavs)):
        basename = path.splitext(path.split(wav_fn)[-1])[0]
        basename = basename.replace("_", "-")

        fbank_fn = path.join(target_dir, basename + ".fbank")

        f.write(wav_fn + " " + fbank_fn + "\n")
    f.close()

    print("Coding raw filterbanks")
    shell(
        "HCopy -T 7 -A -D -V -S " + raw_scp + " -C " + config_fn + " > " + 
        path.join(log_dir, args.dataset + ".fbank.raw.log")
        )


if __name__ == "__main__":
    main()
