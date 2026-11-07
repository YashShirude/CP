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
    arr = []
    for i in range(2):
        arr.append(inlt())
    side1 = arr[0][0] < arr[0][1]
    side2 = arr[1][0] < arr[1][1]
    height1 = arr[0][0] < arr[1][0]
    height2 = arr[0][1] < arr[1][1]

    if side1 & side2 & height1 & height2:
        print("YES")
        return
    if ((not side1) and (not side2) and height1 and height2) or (side1 & side2 & (not height1) and (not height2)):
        print("YES")
        return
    if (not side1) & (not side2) &(not height1) &(not height2):
        print("YES")
        return
    print("NO")


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