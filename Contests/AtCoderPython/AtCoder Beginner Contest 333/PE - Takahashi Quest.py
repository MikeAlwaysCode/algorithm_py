import sys
from collections import Counter

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
    cnt = Counter()
    adv = []
    for _ in range(n):
        adv.append(tuple(mint()))
    op = [0] * n
    for i in range(n - 1, -1, -1):
        t, x = adv[i]
        if t == 2:
            cnt[x] += 1
            op[i] = -1
        elif cnt[x]:
            cnt[x] -= 1
            op[i] = 1
    if any(cnt.values()):
        print(-1)
        return
    ans = c = 0
    av = []
    for o in op:
        c += o
        ans = max(ans, c)
        if o != -1:
            av.append(o)
    print(ans)
    print(*av)


solve()
