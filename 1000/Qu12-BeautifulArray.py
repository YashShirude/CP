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
    n, k, b, s = invr()
    obtained_b = s // k
    arr = [0] * n

    if obtained_b == b:
        arr[0] = s
        for i in arr:
            print(str(i) + " ")
        print("\n")
        return

    if obtained_b < b:
        print("-1\n")
        return

    allowed_extra = n * (k - 1)

    if (b*k) + allowed_extra >= s:
        rem_sum = s - (b*k + k - 1)
        print(str(b*k + k - 1))
        for i in range(1,n):
            sub = min(rem_sum, k-1)
            print(" " + str(sub))
            rem_sum -= sub
        print("\n")
        return
    print("-1\n")
    



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