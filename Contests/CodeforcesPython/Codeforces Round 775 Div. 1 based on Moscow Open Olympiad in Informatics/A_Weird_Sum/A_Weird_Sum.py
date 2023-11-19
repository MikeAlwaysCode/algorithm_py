import sys
from collections import Counter, defaultdict

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, m = mint()

    cnt = Counter()
    pres = Counter()
    pos = defaultdict(list)
    ans = 0

    for i in range(n):
        c = ints()
        for j, x in enumerate(c):
            ans += cnt[x] * i - pres[x]
            cnt[x] += 1
            pres[x] += i
            pos[x].append(j)
    
    for x, p in pos.items():
        ps = 0
        p.sort()
        for i, j in enumerate(p):
            ans += i * j - ps
            ps += j
    print(ans)

solve()