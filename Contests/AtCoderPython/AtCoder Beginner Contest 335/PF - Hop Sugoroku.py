import sys
from collections import Counter

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    nums = ints()
    dp = [0] * n
    dp[0] = 1
    ans = 0
    cnt = Counter()
    s = [set() for _ in range(n)]
    for i in range(n):
        for a in s[i]:
            dp[i] = (dp[i] + cnt[a * n + (i % a)]) % MOD
            if i + a < n:
                s[i + a].add(a)
        ans = (ans + dp[i]) % MOD
        if i + nums[i] < n:
            s[i + nums[i]].add(nums[i])
            cnt[nums[i] * n + (i % nums[i])] = (cnt[nums[i] * n + (i % nums[i])] + dp[i]) % MOD
    print(ans)


solve()
