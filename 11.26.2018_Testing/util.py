#!/usr/bin/env python

from numba import jit, prange, njit
import numpy as np
import time

def go_slow(x):
    for i in range(14):
        x *= x

#@jit(nopython=True, parallel=True)
def go_fast(x):
    for i in range(14):
        x *= x

#@njit(parallel=True)
def parallel():
    for i in prange(4):
        y = i ** 10000000

def nonparallel():
    for i in range(4):
        y = i ** 10000000

def speed_test():
    parallel()
    start = time.time()
    parallel()
    end = time.time()
    print("Elapsed fast (after compilation) = %s" % (end - start))
    fast = end - start
    start = time.time()
    nonparallel()
    end = time.time()
    print("Elapsed slow (after compilation) = %s" % (end - start))
    slow = end - start
    print('Fast way is %i times faster' % (slow / fast))

def read_lengths(fastqs, limit):
    from collections import defaultdict

    lengths = defaultdict(list)

    for sample in fastqs:
        target = open(fastqs[sample], 'r')
        temp_limit = limit

        count = 1
        for line in target:
            if temp_limit > 0:
                if count == 2:
                    lengths[sample].append(len(line))
                    temp_limit -= 1
                if count == 4:
                    count = 0
                count += 1
            if temp_limit == 0:
                break

    return lengths
















