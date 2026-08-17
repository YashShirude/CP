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

def findSecondMin(arr):
    first = sys.maxsize
    second = sys.maxsize
    for num in arr:
        if num < first:
            second = first
            first = num
        elif num < second:
            second = num
    return (first,second)

# 3. Core Logic Function
def solve():
    no_of_arrays = inp()
    min_of_all = sys.maxsize
    min_of_seconds = sys.maxsize
    result = 0
    for i in range(no_of_arrays):
        length_of_array = inp()
        arr = inlt()
        first, second = findSecondMin(arr)
        result += second
        min_of_seconds = min(second,min_of_seconds)
        min_of_all = min(first, min_of_all)
    result -= min_of_seconds
    result += min_of_all
    print(str(result) + "\n")


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





