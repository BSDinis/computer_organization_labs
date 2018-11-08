#!/usr/bin/python3

import os
import sys
import math

def frameMemoryCost():
    return 1/8 * 0.01 

def cacheL1_access_time(ways):
    return 2 * (0.75 + 0.25 * math.log2(ways));

def cacheL1_price(bytes):
    return bytes * 9 / (2**20)

def cacheL2_access_time(ways):
    return 7.5 + 2.5 * math.log2(ways);

def cacheL2_price(bytes):
    return bytes * 0.4 / (2**20)

def ex231():
    print("Compulsory misses: the cache starts up empty, therefore, the data has to be loaded from memory. These are unavoidable misses")
    print("Capacity misses: when the cache is full, new blocks need to replace older blocks - resulting in a miss")
    print("Conflict misses: if memory accesses have the same cache indices, but different tags, they will be replacing each other continuously")
    print("Write-through: a cache write is immediately written to memory")
    print("Write-back: a cache write sets on a dirty bit. On replacement, the write is propagated to memory")

def ex232():
    miss_rates = {
            256: {8: 0.1960, 16: 0.1829, 32: 0.2288, 64:0.3340},
            512: {8: 0.1247, 16: 0.1184, 32: 0.1492, 64:0.2021},
            1024: {8: 0.0305, 16: 0.0363, 32: 0.0770, 64:0.1181},
            }
    n = 1
    cost = cacheL1_price(n) + frameMemoryCost()
    while cost <= 0.011:
        old_cost = cost
        n *= 2
        cost = cacheL1_price(n * 2) + frameMemoryCost()
        

    print(f"frame buffer memory: {frameMemoryCost()} €")
    print(f"cache price: {cacheL1_price(n)} €")
    print(f"price: {old_cost} €")
    print(f"size: {n} B")
    print()

    min1 = {'size': 256, 'bsize': 16, 'rate': miss_rates[256][16]}
    min2 = {'size': 256, 'bsize': 8, 'rate': miss_rates[256][8]}

    for size in miss_rates:
        for bsize in miss_rates[size]:
            print(f"{size} {bsize}\t:::\t{miss_rates[size][bsize]}")
            if size * miss_rates[size][bsize] < min1['size'] * min1['rate']:
                min2 = min1
                min1 = {'size': size, 'bsize': bsize, 'rate': miss_rates[size][bsize]};
            elif size * miss_rates[size][bsize] < min2['size'] * min2['rate']:
                min2 = {'size': size, 'bsize': bsize, 'rate': miss_rates[size][bsize]};

    print(str(min1) + " cost: " + str(cacheL1_price(min1['size']) * min1['rate']))
    print(str(min2) + " cost: " + str(cacheL1_price(min2['size']) * min2['rate']))

def ex233():
    compulsory_fraction = {
            16: {1: 0.0106, 2: 0.0106, 4: 0.2444, 8: 0.2413},
            8: {1: 0.0254, 2: 0.0216, 4: 0.2859, 8: 0.2876}
            }

    capacity_fraction = {
            16: {1: 0.0303, 2: 0.0329, 4: 0.7556, 8: 0.7587},
            8: {1: 0.0561, 2: 0.0488, 4: 0.7059, 8: 0.7080}
            }

    conflict_fraction = {
            16: {1: 0.9591, 2: 0.9565, 4: 0.0000, 8: 0.0000},
            8: {1: 0.9186, 2: 0.9295, 4: 0.0082, 8: 0.0044}
            }

    miss_rate = {
            16: {1: 0.0363, 2: 0.0364, 4: 0.0016, 8: 0.0016},
            8: {1: 0.0305, 2: 0.0357, 4: 0.0027, 8: 0.0027}
            }

    hit_time = { 16: {}, 8: {}}
    miss_time = 150

    for bsize in {8, 16}:
        for ways in range(4):
            miss_r = miss_rate[bsize][2**ways]
            print(f"1024 - {bsize} - {2**ways} - Compulsory - {compulsory_fraction[bsize][2**ways] * miss_r}")
            print(f"1024 - {bsize} - {2**ways} - Capacity - {capacity_fraction[bsize][2**ways] * miss_r}")
            print(f"1024 - {bsize} - {2**ways} - Conflict - {conflict_fraction[bsize][2**ways] * miss_r}")
            print(f"1024 - {bsize} - {2**ways} - Total - {miss_r}")

    print(f"AMAT for architecture w/ L1 cache::")
    print(f"hit_time * (hit_rate) + miss_time * miss_rate")
    print(f"hit_time = 1.5 + 0.5 * log_2(#ways)")
    print(f"hit_rate = 1 - miss_rate")
    print(f"miss_time = 150")
    print(f"AMAT: (1.5 + 0.5 * log_2(#ways) ) * (1 - miss_rate) + 150 * miss_rate")


    for bsize in {8, 16}:
        for ways in range(4):
            hit_time[bsize][2**ways] = cacheL1_access_time(2**ways)
            miss_r = miss_rate[bsize][2**ways]
            hit_r = hit_time[bsize][2**ways]
            price = cacheL1_price(1024)
            print(f"1024 - {bsize} - {2**ways}\t- Miss_Rate::{miss_r}\t- AMAT::{str(1.5 + 0.5 * ways * (1 -  miss_r) + 150 * miss_r)[:5]}\t- Price::{price}\t- Cost::{price * miss_r}")

    print("Given that there are much fewer writes than reads, that we never write to the memory addresses we wish to read (the macroblocks) and the expensive operation is to compute the minimum SAD (which requires a lot of sequential accesses to the macroblocks) a write not allocate coupled with a write through makes sense. Also note that we only write the minimum SAD and the minimizer pair (i, j) and we don't read back from them nor do we write back right after their being written")
    print()
    print()
    print("==And the winner is==")
    bsize = 16
    ways = 2
    hit_time[bsize][2**ways] = cacheL1_access_time(2**ways)
    miss_r = miss_rate[bsize][2**ways]
    hit_r = hit_time[bsize][2**ways]
    price = cacheL1_price(1024)
    print(f" 1024 \n {bsize} \n {2**ways}\t\n Write Through & Write Not-Allocate\t\n Miss_Rate::{miss_r}\t\n AMAT::{str(1.5 + 0.5 * ways * (1 -  miss_r) + 150 * miss_r)[:5]}\t\n Price::{price}\t\n Cost::{price * miss_r}")

                                                                                                                                                   
def ex241():
    n = 1
    base_cost = cacheL1_price(1024) + frameMemoryCost()
    cost = cacheL2_price(n) + base_cost
    while cost <= 0.011:
        old_cost = cost
        n *= 2
        cost = cacheL2_price(n * 2) + base_cost
        

    print(f"frame buffer memory: {frameMemoryCost()} €")
    print(f"L1 cache price: {cacheL1_price(1024)} €")
    print(f"L2 cache price: {cacheL2_price(n)} €")
    print(f"price: {old_cost} €")
    print(f"L1 size: {1024} B")
    print(f"L2 size: {n} B")
    print()

    l1_bsize = 16

    miss_rates =      		{ 16: .6117, 32: 0.3594, 64: 0.2985, 128: .2779}
    compulsory_fraction = 	{ 16: .2444, 32: 0.2488, 64: 0.1498, 128: .2444}
    capacity_fraction = 	{ 16: .7556, 32: 0.6528, 64: 0.8026, 128: .7556}
    conflict_fraction = 	{ 16: .0000, 32: 0.0984, 64: 0.0476, 128: .2779}
    for bsize in miss_rates:
        print(f"L2 Cache:: Bsize = {bsize}\t-- Compulsory\t= {compulsory_fraction[bsize] * miss_rates[bsize]}")
        print(f"L2 Cache:: Bsize = {bsize}\t-- Capacity\t= {capacity_fraction[bsize] * miss_rates[bsize]}")
        print(f"L2 Cache:: Bsize = {bsize}\t-- Conflict\t= {conflict_fraction[bsize] * miss_rates[bsize]}")
        print(f"L2 Cache:: Bsize = {bsize}\t-- Miss Rate\t= {miss_rates[bsize]}\t\t-- Penalty = {miss_rates[bsize] * bsize}")


ex231()
print()
ex232()
print()
ex233()
print()
ex241()
print()
