#!/usr/bin/env python
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import math
import os
import sys

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

    even_index_no = []
    odd_index_no = []

    for i in range(n):
        if i % 2 == 0:
            even_index_no.append(arr[i])
        else:
            odd_index_no.append(arr[i])
    even_gcd = math.gcd(*even_index_no)
    odd_gcd = math.gcd(*odd_index_no)

    flag1 = True
    flag2 = True
    for i in range(n):
        if i % 2 == 0 and arr[i] % odd_gcd == 0:
            flag1 = False
        if i % 2 != 0 and arr[i] % even_gcd == 0:
            flag2 = False
    if flag1:
        print(odd_gcd)
    elif flag2:
        print(even_gcd)
    else:
        print(0)
    return



    


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