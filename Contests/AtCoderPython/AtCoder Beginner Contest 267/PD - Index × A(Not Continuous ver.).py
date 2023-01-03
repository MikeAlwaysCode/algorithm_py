from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

def solve() -> None:
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = [[- 10 ** 18] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = 0
    for i in range(1, n+1):
        dp[i][0] = 0
        # for j in range(1, i+1):
        for j in range(1, min(i+1, m+1)):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + j * arr[i-1])
    
    print(dp[n][m])
    '''
    res = - 10 ** 18
    for i in range(n):
        dp[i][0] = 0
        for j in range(min(i + 1, m)):
            dp[i + 1][j + 1] = max(dp[i][j] + arr[i] * (j + 1), dp[i][j + 1])

    for i in range(m + 1, n + 1):
        res = max(res, dp[i][m])

    print(res)
    '''
solve()