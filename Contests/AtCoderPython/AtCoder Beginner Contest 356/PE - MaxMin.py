import sys
from collections import Counter
# from bisect import bisect_left

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
    ans = 0
    cnt = Counter(nums)
    mx = max(nums)
    d = [0] * (mx + 1)
    for x in set(nums):
        for j in range(x, mx + 1, x):
            d[j] += cnt[x]
    c = 0
    for i, c1 in enumerate(d):
        c += c1
        if cnt[i]:
            ans += c * cnt[i] - cnt[i] * cnt[i] + cnt[i] * (cnt[i] - 1) // 2

    print(ans)


solve()
