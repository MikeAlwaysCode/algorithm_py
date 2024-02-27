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
    nums = ints()
    cnt = Counter()
    ans = 0
    for x in nums:
        if x == 0:
            cnt[x] += 1
            continue
        cc = Counter()
        d = 2
        while d * d <= x:
            while x % d == 0:
                cc[d] += 1
                x //= d
            if x == 1:
                break
            d += 1
        if x > 1:
            cc[x] += 1
        cur = 1
        for k, v in cc.items():
            if v & 1:
                cur *= k
        ans += cnt[cur]
        cnt[cur] += 1
    ans += (n * 2 - cnt[0] - 1) * cnt[0] // 2
    print(ans)


solve()
