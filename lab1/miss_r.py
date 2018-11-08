#!/usr/bin/python3

import os
import sys


def construct_dinero_call(size, bsize, ways, inputfile, outputfile):
    base_prog = "d4-7/dineroIV"
    l1_size = "-l1-usize " + str(size)
    l1_bsize = "-l1-ubsize " + str(bsize)
    l1_assoc = "-l1-uassoc " + str(ways)
    return base_prog + " " + l1_size + " " + l1_bsize + " " + l1_assoc + " < " + inputfile + " > " + outputfile

def construct_dinero_call_flag(size, bsize, ways, inputfile, outputfile, flags):
    base_prog = "d4-7/dineroIV"
    l1_size = "-l1-usize " + str(size)
    l1_bsize = "-l1-ubsize " + str(bsize)
    l1_assoc = "-l1-uassoc " + str(ways)
    return base_prog + " " + flags + " " + l1_size + " " + l1_bsize + " " + l1_assoc + " < " + inputfile + " > " + outputfile

def construct_dinero_call2(bsize, ways, inputfile, outputfile):
    base_prog = "d4-7/dineroIV"
    l1_size = "-l1-usize " + str(1024)
    l1_bsize = "-l1-ubsize " + str(16)
    l1_assoc = "-l1-uassoc " + str(4)
    l2_size = "-l2-usize " + str(2048)
    l2_bsize = "-l2-ubsize " + str(bsize)
    l2_assoc = "-l2-uassoc " + str(ways)
    return base_prog + \
 " " + \
 l1_size + \
 " " +  \
 l1_bsize +\
 " " +\
 l1_assoc +\
 " " +\
 l2_size +\
 " " +\
 l2_bsize +\
 " " +\
 l2_assoc +\
 " < " +\
 inputfile +\
 " > " +\
 outputfile

def construct_dinero_call2_flag(bsize, ways, inputfile, outputfile, flags):
    base_prog = "d4-7/dineroIV"
    l1_size = "-l1-usize " + str(1024)
    l1_bsize = "-l1-ubsize " + str(16)
    l1_assoc = "-l1-uassoc " + str(4)
    l2_size = "-l2-usize " + str(2048)
    l2_bsize = "-l2-ubsize " + str(bsize)
    l2_assoc = "-l2-uassoc " + str(ways)
    return base_prog + " " + flags + " " + l1_size + " " + l1_bsize + " " + l1_assoc + " " + l2_size + " " + l2_bsize + " " + l2_assoc + " < " + inputfile + " > " + outputfile

sizes = [1024, 512, 256]
bsizes = [8, 16, 32, 64]

'''
for size in sizes:
    for bsize in bsizes:
        os.system(construct_dinero_call(size, bsize, 1, "trace.log", "dinero_trace_"+str(size)+"_"+str(bsize)+".log"))

for i in range(4):
    os.system(construct_dinero_call_flag(1024,
        8,
        2**i,
        "trace.log",
        "dinero_trace_"+str(1024)+"_"+str(8)+"_"+str(2**i)+"ways_extra.log",
        "-l1-uccc"))
    os.system(construct_dinero_call_flag(1024, 16, 2**i, "trace.log", "dinero_trace_"+str(1024)+"_"+str(16)+"_"+str(2**i)+"ways_extra.log", "-l1-uccc"))

os.system(construct_dinero_call_flag(1024, 16, 4, "trace.log", "dinero_trace_"+str(1024)+"_"+str(16)+"_"+str(4)+"ways_extra_alloc_wback.log", "-l1-uccc -l1-uwalloc a -l1-uwback a"))
os.system(construct_dinero_call_flag(1024, 16, 4, "trace.log", "dinero_trace_"+str(1024)+"_"+str(16)+"_"+str(4)+"ways_extra_alloc_wthrough.log", "-l1-uccc -l1-uwalloc a -l1-uwback n"))
os.system(construct_dinero_call_flag(1024, 16, 4, "trace.log", "dinero_trace_"+str(1024)+"_"+str(16)+"_"+str(4)+"ways_extra_around_wback.log", "-l1-uccc -l1-uwalloc n -l1-uwback a"))
os.system(construct_dinero_call_flag(1024, 16, 4, "trace.log", "dinero_trace_"+str(1024)+"_"+str(16)+"_"+str(4)+"ways_extra_around_wthrough.log", "-l1-uccc -l1-uwalloc n -l1-uwback n"))

os.system(construct_dinero_call_flag(1024, 16, 8, "trace.log", "dinero_trace_"+str(1024)+"_"+str(16)+"_"+str(8)+"ways_extra_alloc_wback.log", "-l1-uccc -l1-uwalloc a -l1-uwback a"))
os.system(construct_dinero_call_flag(1024, 16, 8, "trace.log", "dinero_trace_"+str(1024)+"_"+str(16)+"_"+str(8)+"ways_extra_alloc_wthrough.log", "-l1-uccc -l1-uwalloc a -l1-uwback n"))
os.system(construct_dinero_call_flag(1024, 16, 8, "trace.log", "dinero_trace_"+str(1024)+"_"+str(16)+"_"+str(8)+"ways_extra_around_wback.log", "-l1-uccc -l1-uwalloc n -l1-uwback a"))
os.system(construct_dinero_call_flag(1024, 16, 8, "trace.log", "dinero_trace_"+str(1024)+"_"+str(16)+"_"+str(8)+"ways_extra_around_wthrough.log", "-l1-uccc -l1-uwalloc n -l1-uwback n"))
'''

l1_bsize = 16
for i in range(4):
    os.system(construct_dinero_call2(2**i * l1_bsize, 1, "trace.log", "dinero_trace_l2_2048_"+str(2**i * l1_bsize)+".log"))
    os.system(construct_dinero_call2_flag(
        2**i * l1_bsize,
        1,
        "trace.log",
        "dinero_trace_l2_2048_+"+str(int(2**i * l1_bsize))+"_1_ways_extra.log",
        "-l1-uccc -l2-uccc"))
