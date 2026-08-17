import sys

input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    monsters = []

    for i in range(n):
        rem = a[i] % k
        if rem == 0:
            rem = k

        monsters.append((rem, i))

    monsters.sort(key=lambda x: (-x[0], x[1]))

    print(*(i + 1 for _, i in monsters))


t = int(input())

for _ in range(t):
    solve()