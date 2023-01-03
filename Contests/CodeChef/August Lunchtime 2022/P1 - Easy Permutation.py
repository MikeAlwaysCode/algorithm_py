from collections import Counter, defaultdict

def solve() -> None:
    n = int(input())

    ans = [n-x for x in range(n)]

    print(*ans)

t = int(input())
for _ in range(t):
    solve()