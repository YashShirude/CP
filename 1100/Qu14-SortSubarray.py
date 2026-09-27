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
    a = inlt()
    a_dash = inlt()

    min_pointer = float("inf")
    max_pointer = 0

    for i in range(n):
        if a[i] != a_dash[i]:
            min_pointer = min(min_pointer, i)
            max_pointer = max(max_pointer, i)
    
    prev = a_dash[min_pointer]
    i = min_pointer
    while i >= 0:
        if a_dash[i] <= prev:
            min_pointer = i
        else:
            break
        prev = a_dash[i]
        i -= 1
    prev = a_dash[max_pointer]
    j = max_pointer
    while j < n:
        if a_dash[j] >= prev:
            max_pointer = j
        else:
            break
        prev = a_dash[j]
        j += 1
    l = min_pointer + 1
    r = max_pointer + 1
    print(str(l) + " " + str(r))


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