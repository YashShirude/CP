#!/usr/bin/env python
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import math
import os
import sys

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
    n = inp()
    if(n % 2 == 0):
        print(str(int(n/2)) + " " + str(int(n/2)) + "\n")
        return
    min_factor = float('inf')
    factors_product = 1
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors_product *= factor
            min_factor = min(min_factor, factor)
            n //= factor
        factor += 2
        
    # 3. If n is still greater than 2, the remaining n is prime
    if n > 2:
        factors_product *= n
        min_factor = min(min_factor,n)
    a = int(factors_product/ min_factor)
    b = int(a * (min_factor - 1))
    print(str(a) + " " + str(b) + "\n")


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