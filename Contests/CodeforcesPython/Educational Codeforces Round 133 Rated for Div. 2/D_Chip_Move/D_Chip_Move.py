MOD = 998244353

def solve() -> None:
    n, k = map(int, input().split())
    dp = [0] * (n+1)
    ans = [0] * (n+1)
    dp[0] = 1
    mn = 0
    while mn + k <= n:
        sum = [0] * k
        for i in range(mn, n+1):
            cur = dp[i]
            dp[i] = sum[i % k]
            sum[i % k] = (sum[i % k] + cur) % MOD
            ans[i] = (ans[i] + dp[i]) % MOD
        mn += k
        k += 1
    print(*ans[1:])

# t = int(input())
# for _ in range(t):
solve()