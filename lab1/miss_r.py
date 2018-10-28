#!/usr/bin/python3

import os
import sys


def construct_dinero_call(size, bsize, ways, inputfile, outputfile):
    base_prog = "d4-7/dineroIV"
    l1_size = "-l1-usize " + str(size)
    l1_bsize = "-l1-ubsize " + str(bsize)
    l1_assoc = "-l1-uassoc " + str(ways)
    return base_prog + " " + l1_size + " " + l1_bsize + " " + l1_assoc + " < " + inputfile + " > " + outputfile


sizes = [1024, 512, 256]
bsizes = [8, 16, 32, 64]

for size in sizes:
    for bsize in bsizes:
        os.system(construct_dinero_call(size, bsize, 1, "trace.log", "dinero_trace_"+str(size)+"_"+str(bsize)+".log"))

