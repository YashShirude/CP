#!/usr/bin/env python
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import math
import os
import sys
import heapq

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
    n, p = invr()
    a = inlt()
    b = inlt()
    combined_list = [{"a": x, "b": y} for x, y in zip(a,b)]
    sorted_list = sorted(combined_list, key=lambda x: x["b"])

    cost = p
    i = 0
    j = 0
    while j < n - 1:
        people = sorted_list[i]["a"]
        transfer_cost = sorted_list[i]["b"]
        if transfer_cost > p:
            cost += (n - j - 1) * p
            print(str(cost)+"\n")
            return
        min_no_of_people = min(n - j - 1, people)
        j += min_no_of_people
        cost += (min_no_of_people * transfer_cost)
        i += 1
    print(str(cost)+"\n")


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