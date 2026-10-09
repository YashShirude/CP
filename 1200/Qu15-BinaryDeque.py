import sys

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); s = int(data[idx + 1]); idx += 2
        a = data[idx:idx + n]
        idx += n
        a = [int(x) for x in a]
        if sum(a) < s:
            out.append("-1")
            continue
        best = 0  # empty subarray is allowed (matters when s == 0)
        l = 0
        cur = 0
        for r in range(n):
            cur += a[r]
            while cur > s:
                cur -= a[l]
                l += 1
            if cur == s and r - l + 1 > best:
                best = r - l + 1
        out.append(str(n - best))
    print("\n".join(out))

main()