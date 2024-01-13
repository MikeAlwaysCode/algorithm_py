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
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    cnt = Counter()
    ans = 0
    for _ in range(n):
        s = input()
        mn = cur = 0
        for c in s:
            if c == '(':
                cur += 1
            else:
                cur -= 1
            mn = min(mn, cur)
        if (cur >= 0 and mn == 0) or (cur < 0 and mn == cur):
            cnt[cur] += 1
            if cur:
                ans += cnt[-cur]
    ans += cnt[0] * cnt[0]
    print(ans)
 

solve()
