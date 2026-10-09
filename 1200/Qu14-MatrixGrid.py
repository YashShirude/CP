import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        g = data[idx:idx + n]; idx += n
        ans = 0
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                s = (int(g[i][j])
                     + int(g[j][n - 1 - i])
                     + int(g[n - 1 - i][n - 1 - j])
                     + int(g[n - 1 - j][i]))
                ans += min(s, 4 - s)
        out.append(str(ans))
    print("\n".join(out))

main()