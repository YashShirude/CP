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
    n, k, a, b = invr()
    coordinates = []
    for i in range(n):
        x, y = invr()
        coordinates.append((x,y))

    closest_major_dist_to_a = float('inf')
    closest_major_dist_to_b = float('inf')

    if a <= k:
        closest_major_dist_to_a = 0
    else:
        xa, ya = coordinates[a-1]
        for i in range(k):
            x,y = coordinates[i]
            dist = abs(xa - x) + abs(ya - y)
            closest_major_dist_to_a = min(dist, closest_major_dist_to_a)
    if b <= k:
        closest_major_dist_to_b = 0
    else:
        xb, yb = coordinates[b-1]
        for i in range(k):
            x,y = coordinates[i]
            dist = abs(xb - x) + abs(yb - y)
            closest_major_dist_to_b = min(dist, closest_major_dist_to_b)

    
    xa, ya = coordinates[a-1]
    xb, yb = coordinates[b-1]
    answer = min(closest_major_dist_to_a + closest_major_dist_to_b, abs(xa-xb) + abs(ya-yb))
    print(answer)

    



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