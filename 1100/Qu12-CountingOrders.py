#!/usr/bin/env python
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import math
import os
import sys
import cmath

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

def find_roots(a, b, c):
    # Ensure it's a valid quadratic equation
    if a == 0:
        return "Coefficient 'a' cannot be zero."

    # Calculate the discriminant: b² - 4ac
    discriminant = (b**2) - (4*a*c)
    
    # Calculate both roots using the quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

    if root1.real > 0:
        return int(root1.real)
    elif root2.real > 0:
        return int(root2.real)
    
    return None

# 3. Core Logic Function
def solve():
    n = inp()
    arr1 = inlt()
    arr2 = inlt()

    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)

    pointer1 = 0
    pointer2 = 0
    result = 1
    mod = 10**9 + 7

    while pointer1 < n and pointer2 < n:
        a_num = sorted_arr1[pointer1]
        b_num = sorted_arr2[pointer2]
        if a_num > b_num:
            pointer2 += 1
        else:
            possible_positions = pointer2 - pointer1                
            result = (result * possible_positions) % mod
            pointer1 += 1
    while pointer1 < n:
        possible_positions = n - pointer1
        result = (result * possible_positions) % mod
        pointer1 += 1
    while pointer2 < n:
            print(0)
            return
    print(result)
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