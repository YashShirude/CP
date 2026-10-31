# consonant should not be last except n
# check every character except the last, if consonant and not n the next character should be vowel
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
    s = insr()
    vowels = ['a', 'e', 'i', 'o', 'u']

    if s[-1] not in vowels and s[-1] != 'n':
        print("no")
        return

    for i in range(0,len(s)-1):
        char = s[i]
        if char not in vowels and char != 'n' and s[i+1] not in vowels:
            print("no")
            return
    print("yes")

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