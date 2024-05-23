import sys
from bisect import bisect

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
    n, k, q = mint()
    s = [0] + ints()
    t = [0] + ints()
    ans = []
    for _ in range(q):
        d = sint()
        i = bisect(s, d)
        res = t[i - 1]
        if d > s[i - 1]:
            res += (d - s[i - 1]) * (t[i] - t[i - 1]) // (s[i] - s[i - 1])
        ans.append(res)
    print(*ans)

for _ in range(int(input())):
    solve()
