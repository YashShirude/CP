#!/usr/bin/env python
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import math
import os
import sys
import copy

# 1. Fast I/O Setup
# Overriding input() with sys.stdin.readline drastically reduces I/O time.
input = sys.stdin.readline

def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)

# 2. Quick Input Helper Functions
def inp():
    """Reads a single integer."""
    return int(input())


def invr():
    """Reads multiple space-separated integers as independent variables."""
    return map(int, input().split())


def inlt():
    """Reads space-separated integers into a list."""
    return list(map(int, input().split()))


def insr():
    """Reads a line of string, stripping trailing newlines."""
    return input().strip()


# 3. Core Logic Function
def solve():
    n = inp()
    arr = inlt()
    gap = -1
    l = 0
    r = 0

    for i in range(n-1):
        num_1 = arr[i]
        num_2 = arr[i+1]
        diff = abs(num_1-num_2)
        if diff > gap:
            gap = diff
            l = i
            r = i+1

    arr_1 = copy.copy(arr)
    arr_2 = copy.copy(arr)
    arr_3 = copy.copy(arr)
    arr_4 = copy.copy(arr)


    if l != 0:
        arr_1[l] = 2*arr[l-1]
        arr_1[l-1] = 2*arr[l]
    if r != n-1:
            arr_2[r] = 2*arr[r+1]
            arr_2[r+1] = 2*arr[r]
    arr_3[l] = 2*arr[l]
    arr_4[r] = 2*arr[r]
    
    gap_1 = -1
    gap_2 = -1
    gap_3 = -1
    gap_4 = -1
    for i in range(n-1):
        num_11 = arr_1[i]
        num_12 = arr_1[i+1]
        num_21 = arr_2[i]
        num_22 = arr_2[i+1]
        num_31 = arr_3[i]
        num_32 = arr_3[i+1]
        num_41 = arr_4[i]
        num_42 = arr_4[i+1]
        diff_1 = abs(num_11-num_12)
        diff_2 = abs(num_21-num_22)
        diff_3 = abs(num_31-num_32)
        diff_4 = abs(num_41-num_42)
        gap_1 = max(gap_1,diff_1)
        gap_2 = max(gap_2,diff_2)
        gap_3 = max(gap_3,diff_3)
        gap_4 = max(gap_4,diff_4)

    if gap_1 == -1:
        gap_1 = float('inf')
    if gap_2 == -1:
        gap_2 = float('inf')
    if gap_3 == -1:
        gap_3 = float('inf')
    if gap_4 == -1:
        gap_4 = float('inf')
    print(min(gap,min(gap_1,min(gap_2,min(gap_3,gap_4)))))

# 4. Main Execution Block & File Redirection
def main():
    # Automatically switch to local file I/O if input.txt exists on your machine
    if os.path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")

    # Set a high recursion limit to prevent crashes on deep DFS/tree algorithms
    sys.setrecursionlimit(200000)

    # Read number of test cases (Defaults to 1 if not specified)
    try:
        t = int(input())
    except (ValueError, TypeError):
        t = 1

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()