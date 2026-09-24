import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    total = sum(arr)
    arr.sort()

    # prefix[i] = sum of the i smallest *pairs* (2*i smallest elements), i = 0..k
    prefix = [0] * (k + 1)
    for i in range(k):
        prefix[i + 1] = prefix[i] + arr[2 * i] + arr[2 * i + 1]

    # suffix[j] = sum of the j largest elements, j = 0..k
    suffix = [0] * (k + 1)
    for j in range(k):
        suffix[j + 1] = suffix[j] + arr[n - 1 - j]

    min_loss = min(prefix[i] + suffix[k - i] for i in range(k + 1))
    print(total - min_loss)

def main():
    t = int(input())
    out = []
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()