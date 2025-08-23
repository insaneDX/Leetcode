#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    swaps = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] or arr[i] == i + 1:
            continue

        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr[j] - 1 # next index to visit
            cycle_size += 1

        if cycle_size > 0:
            swaps += cycle_size - 1 # A cycle of k elements requires exactly k - 1 swaps to sort.

    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')
    fptr.close()

# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

