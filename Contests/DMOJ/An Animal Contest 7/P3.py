from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

def solve() -> None:
    MOD = 10 ** 9 + 7

    n, m = map(int, input().split())
    arrp = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    portal = [0] * n
    for i, p in enumerate(arrp):
        portal[p-1] = arrp[i-1]-1
    
    cnt = [0] * (n + 1)
    for i, a in enumerate(arr):
        cnt[i+1] = cnt[i] + a
    
    dp = [[0] * n for _ in range(n)]

    ans = 0
    for i in range(n-2, -1, -1):
        for j in range(i + 1, n):
            if portal[i] and portal[j]:
                continue
            dp[i][j] = cnt[j] - cnt[i]
            if portal[i]:
                if portal[i] < j:
                    dp[i][j] = min(dp[i][j], cnt[j] - cnt[portal[i]])
                else:
                    dp[i][j] = min(dp[i][j], cnt[portal[i]] - cnt[j])
            if portal[j]:
                if portal[j] > i:
                    dp[i][j] = min(dp[i][j], cnt[portal[j]] - cnt[i])
                else:
                    dp[i][j] = min(dp[i][j], cnt[i] - cnt[portal[j]])

            ans += dp[i][j]
            ans %= MOD
    print(dp)
    print(ans)

# t = int(input())
# for _ in range(t):
solve()