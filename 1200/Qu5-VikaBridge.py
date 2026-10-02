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
    n, k = invr()
    arr = inlt()
    
    hashmap = dict()
    default = {
        'prev': 0,
        'max_jump': 0 
    }
    for i in range(n):
        num = arr[i]
        values = hashmap.get(str(num), default)
        start_dist = values['prev']
        max_jump = values['max_jump'] 
        end_dist = n
        max_jump = max(max_jump, max(i - start_dist, end_dist - i - 1))
        hashmap[str(num)] = {
            'prev': i,
            'max_jump': max_jump
        }
    min_jump = float('inf')
    for key in hashmap.keys():
        min_jump = min(min_jump,hashmap[key]['max_jump'])
    min_jump_after_coloring = min_jump//2
    print(min_jump_after_coloring)



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