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
    num = inp()

    arr = []
    while num > 0:
        curr = num % 10
        num = num // 10
        arr.append(curr)
    arr.reverse()

    even_at_even = False
    odd_at_odd = False
    for i in range(n):
        num = arr[i]
        index = i + 1
        if index % 2 == 0 and num % 2 == 0:
            even_at_even = True
        if index % 2 == 1 and num % 2 == 1:
            odd_at_odd = True

    
    if n % 2 == 1 and odd_at_odd:
        print(1)
    elif n % 2 == 0 and even_at_even:
        print(2)
    else:
        if n % 2 == 0:
            print(1)
        else:
            print(2)




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