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
    # n = inp()
    # arr = inlt()

    # hashmap = dict()
    # for num in arr:
    #     hashmap[num] = hashmap.get(num,0) + 1
    # keys = hashmap.keys()
    # sorted_keys = sorted(keys)

    # # print(hashmap)

    # k = len(sorted_keys)
    # prev = sorted_keys[0]
    # min_freq_segment = hashmap[prev]
    # answer = 0
    # for i in range(1,k):
    #     prev = sorted_keys[i-1]
    #     num = sorted_keys[i]
    #     curr_num_freq = hashmap[num]
    #     prev_num_freq = hashmap[prev]
    #     if num == prev + 1:
    #         min_freq_segment = min(min_freq_segment, curr_num_freq)
    #         answer += max(prev_num_freq-curr_num_freq,0)
    #         # print(answer)
    #     else:
    #         answer += prev_num_freq
    #         # print(answer)
    #         min_freq_segment = curr_num_freq
    # answer += min_freq_segment
    # answer += hashmap[sorted_keys[k-1]] - min_freq_segment
    # print(answer)

    # ** same solution but hashmap is causing tle because of collisions
    n = inp()
    arr = sorted(inlt())

    vals, cnts = [], []
    for x in arr:
        if vals and vals[-1] == x:
            cnts[-1] += 1
        else:
            vals.append(x)
            cnts.append(1)

    answer = 0
    for i in range(len(vals)):
        if i > 0 and vals[i - 1] == vals[i] - 1:
            answer += max(cnts[i] - cnts[i - 1], 0)  # new chains starting at vals[i]
        else:
            answer += cnts[i]                        # no x-1 present, all start here
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