from collections import Counter, defaultdict

def solve() -> None:
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = [[0] * n for _ in range(2)]
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1] + ( arr[i-1] ^ arr[i] ), dp[1][i-1] + ( (arr[i-1]+x) ^ arr[i] ))
        dp[1][i] = max(dp[0][i-1] + ( arr[i-1] ^ (arr[i]+x) ), dp[1][i-1] + ( (arr[i-1]+x) ^ (arr[i]+x) ))

    print(max(dp[0][n-1], dp[1][n-1]))

t = int(input())
for _ in range(t):
    solve()