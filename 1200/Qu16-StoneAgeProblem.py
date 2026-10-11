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
    n, q = invr()
    arr = inlt()
    queries = []
    for i in range(q):
        queries.append(inlt())

    hashmap = dict()
    for i in range(n):
        hashmap[str(i+1)] = arr[i]    
    replace_all_num = -1
    prev_sum = sum(arr)
    for query in queries:
        t = query[0]
        num = query[1]
        if t == 1:
            value = query[2]
            initial_value = hashmap.get(str(num),-1)
            if(initial_value == -1):
                initial_value = replace_all_num
            prev_sum += (value - initial_value)
            hashmap.update({str(num):value})
        else:
            replace_all_num = num
            prev_sum = n * num
            hashmap = dict()
        print(prev_sum)



# 4. Main Execution Block & File Redirection
def main():
    # Automatically switch to local file I/O if input.txt exists on your machine
    if os.path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")

    # Set a high recursion limit to prevent crashes on deep DFS/tree algorithms
    sys.setrecursionlimit(200000)

    # Read number of test cases (Defaults to 1 if not specified)
    # try:
    #     t = int(input())
    # except (ValueError, TypeError):
    t = 1

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()