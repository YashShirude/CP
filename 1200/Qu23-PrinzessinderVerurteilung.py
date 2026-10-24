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
    words = insr()

    single_char = 26
    double_char = 26 * 26
    triple_char = 26 * 26 * 26

    hashset = set()

    for char in words:
        hashset.add(char)

    if len(hashset) < single_char:
        for i in range(97,123):
            if chr(i) not in hashset:
                print(chr(i))
                return

    for i in range(n-1):
        char = words[i] + "" + words[i+1]
        hashset.add(char)

    if len(hashset) < single_char + double_char:
            for i in range(97,123):
                for j in range(97,123):
                    word = chr(i) + "" + chr(j)
                    if word not in hashset:
                        print(word)
                        return
    
    for i in range(n-2):
        char = words[i] + "" + words[i+1] + "" + words[i+2]
        hashset.add(char)
    
    if len(hashset) < single_char + double_char + triple_char:
        for i in range(97,123):
            for j in range(97,123):
                for k in range(97,123):
                    word = chr(i) + "" + chr(j) + "" + chr(k)
                    if word not in hashset:
                        print(word)
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