import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    ans = 0

    for _ in range(3):
        stopped = False

        books = list(map(int, input().split()))

        for a in books:
            # Once a book contains a bit not present in x,
            # we cannot take this book or anything below it.
            if stopped:
                continue

            if (a | x) != x:
                stopped = True
                continue

            ans |= a

    print("YES" if ans == x else "NO")