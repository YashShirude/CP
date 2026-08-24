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


# 3. Core Logic Function
def solve():
    n = inp()
    arr1 = inlt()
    arr2 = inlt()

    arr1_dict = {}
    arr2_dict = {}
    prev_num = arr1[0]
    counter = 1

    current_num = prev_num
    ans = 0

    for i in range(1,n):
        current_num = arr1[i]
        if(current_num == prev_num):
            counter += 1
        else:
            arr1_dict[prev_num] = max(arr1_dict.get(prev_num,0), counter)
            prev_num = current_num
            ans = max(ans, counter)
            counter = 1
    arr1_dict[current_num] = max(arr1_dict.get(current_num,0), counter)
    ans = max(ans, counter)


    prev_num = arr2[0]
    counter = 1
    current_num = prev_num
    for i in range(1,n):
        current_num = arr2[i]
        if(current_num == prev_num):
            counter += 1
        else:
            arr2_dict[prev_num] = max(arr2_dict.get(prev_num,0), counter)
            ans = max(ans, counter)
            prev_num = current_num
            counter = 1
    arr2_dict[current_num] = max(arr2_dict.get(current_num,0), counter)
    ans = max(ans, counter)

    min_dict = arr2_dict
    if(len(arr1_dict) < len(arr2_dict)):
        min_dict = arr1_dict

    for key in min_dict:
        ans = max(ans, arr1_dict.get(key,0) + arr2_dict.get(key,0))
    print(str(ans) + "\n")

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