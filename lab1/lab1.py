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

    for bsize in {8, 16}:
        for ways in range(4):
            miss_r = miss_rate[bsize][2**ways]
            print(f"1024 - {bsize} - {2**ways} - Compulsory - {compulsory_fraction[bsize][2**ways] * miss_r}")
            print(f"1024 - {bsize} - {2**ways} - Capacity - {capacity_fraction[bsize][2**ways] * miss_r}")
            print(f"1024 - {bsize} - {2**ways} - Conflict - {conflict_fraction[bsize][2**ways] * miss_r}")
            print(f"1024 - {bsize} - {2**ways} - Total - {miss_r}")




ex231()
print()
ex232()
print()
ex233()
print()
