from collections import Counter, defaultdict

def solve() -> None:
    n, x = map(int, input().split())
    ans = p = 0
    for i in range(0, 30):
        if not x&(1<<i):
            if n&(1<<i):
                ans += (1<<p)
            p += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()