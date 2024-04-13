import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    nums = ints()
    nums.sort()
    s = sum(nums)

    ans = 0
    dp = [0] * (s + 1)
    dp[0] = 1
    for x in nums:
        for i in range(s, -1, -1):
            if dp[i] == 0:
                continue
            dp[i + x] = (dp[i + x] + dp[i]) % MOD
            if x >= i:
                ans = (ans + x * dp[i] % MOD) % MOD
            else:
                ans = (ans + (i + x + 1) // 2 * dp[i] % MOD) % MOD
    print(ans)


solve()
