import sys
from collections import Counter, deque

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    p = ints()
    cnt = [Counter() for _ in range(n)]
    for i in range(n):
        cnt[i] = Counter(ints()[1:])
    ans = [0] * n
    for u in range(n - 1, -1, -1):
        cu = cnt[u]
        m = len(cu)
        for i, v in enumerate(sorted(cu.values())):
            ans[u] = max(ans[u], v * (m - i))
        if u == 0:
            break
        cv = cnt[p[u] - 1]
        if len(cu) > len(cv):
            cu, cv = cv, cu
        for k, v in cu.items():
            cv[k] += v
        cnt[p[u] - 1] = cv
    print(*ans, sep='\n')


solve()
