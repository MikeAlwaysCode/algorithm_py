from collections import Counter, defaultdict

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    inf = 1e9
    dp = [inf] * n
    op = [inf] * (n + 1)
    dp[0] = 0
    op[arr[0]] = 0
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            dp[i] = dp[i-1]
        
        dp[i] = min(dp[i], op[arr[i]] + 1)
        op[arr[i]] = min(op[arr[i]], dp[i])
    # print(op)
    # print(dp)
    print(dp[n-1] if dp[n-1] < n else -1)

t = int(input())
for _ in range(t):
    solve()