

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
    matrix = []
    
    for i in range(n):
        matrix.append(inlt())
    
    total_hits = 0
    for col in range(0,n):
        col_2 = col
        max_neg = 0
        for row in range(n-col):
            num = matrix[row][col_2]
            if num < 0:
                max_neg = min(max_neg, num)
            col_2 += 1
        total_hits += abs(max_neg)
    
    for row in range(1,n):
        row_2 = row
        max_neg=0
        for col in range(n-row):
            num = matrix[row_2][col]
            if num < 0:
                max_neg = min(max_neg, num)
            row_2 += 1
        total_hits += abs(max_neg)
    # print(hits)
    # print(total_neg)
    # print(common_neg)
    print (total_hits)


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