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
    arr1 = inlt()
    arr2 = inlt()
    arr3 = inlt()

    indexed_nums_1 = list(enumerate(arr1))
    indexed_nums_2 = list(enumerate(arr2))
    indexed_nums_3 = list(enumerate(arr3))

    sorted_indexed_nums_1 = sorted(indexed_nums_1, key=lambda x:x[1], reverse=True)[:3]
    sorted_indexed_nums_2 = sorted(indexed_nums_2, key=lambda x:x[1], reverse=True)[:3]
    sorted_indexed_nums_3 = sorted(indexed_nums_3, key=lambda x:x[1], reverse=True)[:3]

    max_sum = 0
    for i in range(3):
        index1, num1 = sorted_indexed_nums_1[i%3]
        for j in range(3):
            index2, num2 = sorted_indexed_nums_2[j%3]
            for k in range(3):
                index3, num3 = sorted_indexed_nums_3[k%3]
                if (index1 != index2) and (index2 != index3) and (index1 != index3):
                    max_sum = max(max_sum, num1 + num2 + num3)
    print(max_sum)

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