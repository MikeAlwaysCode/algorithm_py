import sys
# from collections import Counter

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
    M = 500
    cnt = [[0] * M for _ in range(M)]
    for i in range(n):
        for j in range(1, M):
            dp[i] = (dp[i] + cnt[j][i % j]) % MOD
        ans = (ans + dp[i]) % MOD
        if nums[i] >= M:
            for j in range(i + nums[i], n, nums[i]):
                dp[j] = (dp[j] + dp[i]) % MOD
        elif i + nums[i] < n:
            cnt[nums[i]][i % nums[i]] = (cnt[nums[i]][i % nums[i]] + dp[i]) % MOD
    print(ans)


solve()
