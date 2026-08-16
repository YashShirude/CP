#!/usr/bin/env python
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import math
import os
import sys
import heapq

# 1. Fast I/O Setup
# Overriding input() with sys.stdin.readline drastically reduces I/O time.
input = sys.stdin.readline
print = sys.stdout.write


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
    n, k = invr()
    arr = inlt()
    min_op = 4
    multiples_of_2 = 0
    heap = []
    for i in arr:
        rem = i % k
        if i % 2 == 0:
            multiples_of_2 += 1

        if(rem == 0) or (multiples_of_2 >= 2 and k == 4):
            print("0\n")
            return
        
        min_op = min(min_op, k - rem)
    if k == 4:
        if multiples_of_2 == 1 and n != 1:
            print("1\n")
        elif n != 1 and min_op >= 2:
            print("2\n")
        else:
            print(str(min_op) + "\n")
        return
    print(str(min_op) + "\n")

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