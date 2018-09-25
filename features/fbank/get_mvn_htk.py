#!/usr/bin/env python

"""
Perform mean and variance normalisation.

Author: Herman Kamper
Contact: kamperh@gmail.com
Date: 2015, 2018
"""

from __future__ import division
from __future__ import print_function
from os import path
import argparse
import os
import sys

sys.path.append(path.join(".."))

from utils import shell


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

    # Directory and configuration variables
    scp_dir = path.join(args.dataset, "scp")
    log_dir = path.join(args.dataset, "log")
    config_dir = "config"

    mn_dir = path.join(args.dataset, "mn")
    vn_dir = path.join(args.dataset, "vn")
    mvn_dir = path.join(args.dataset, "mvn")

    mn_config_fn = path.join(config_dir, "mn.conf")
    vn_config_fn = path.join(config_dir, "vn." + args.dataset + ".conf")
    mvn_config_fn = path.join(
        config_dir, "mvn." + args.dataset + ".conf"
        )

    segments_scp_fn = path.join(
        scp_dir, args.dataset + ".fbank.raw.segments.scp"
        )
    mvn_scp_fn = path.join(scp_dir, args.dataset + ".fbank.mvn.scp")
    mvn_coding_scp_fn = path.join(
        scp_dir, args.dataset + ".fbank.mvn.coding.scp"
        )

    for d in [mn_dir, vn_dir, mvn_dir]:
        if not path.isdir(d):
            os.makedirs(d)
    mvn_dir = path.abspath(mvn_dir)

    # Get mask from config
    mask = [
        i.strip().split() for i in open(vn_config_fn) if "CMEANMASK" in i
        ][0][-1]

    print("Getting mean vectors")
    shell(
        "HCompV -A -D -V -T 1 -C " + mn_config_fn + " -c " + mn_dir + " -k "
        + mask
        + " -q m -S " + segments_scp_fn
        )

    print("Getting variance vectors")
    shell(
        "HCompV -A -D -V -T 1 -C " + vn_config_fn + " -c " + vn_dir + " -k "
        + mask
        + " -q v -S " + segments_scp_fn
        )

    print("Writing MVN SCP:", mvn_scp_fn)
    print("Writing MVN coding SCP:", mvn_coding_scp_fn)
    mvn_scp = open(mvn_scp_fn, "w")
    mvn_coding_scp = open(mvn_coding_scp_fn, "w")
    segments_scp = open(segments_scp_fn)
    for line in segments_scp:
        mvn_fbank_fn = path.join(mvn_dir, line.split("=")[0])
        mvn_scp.write(mvn_fbank_fn + "\n")
        mvn_coding_scp.write(line.strip() + " " + mvn_fbank_fn + "\n")
    segments_scp.close()
    mvn_scp.close()
    mvn_coding_scp.close()

    # Get unit covariance file
    unit_covar_fn = "unit.covar"
    f = open(unit_covar_fn, "w")
    f.write("<VARSCALE> 40\n")
    f.write(" 1.000000e+00" *40)
    f.close()

    print("Coding to MVN")
    shell(
        "HCopy -T 7 -A -D -V -S " + mvn_coding_scp_fn + " -C " +
        mvn_config_fn + " > " + path.join(log_dir, "mvn.log")
        )

    os.remove(unit_covar_fn)


if __name__ == "__main__":
    main()
