from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

x = [0] * (10**5 + 1)
a = [0] * (10**5 + 1)
n = int(input())

maxt = 0
for _ in range(n):
    t, cx, ca = map(int, input().split())
    x[t] = cx
    a[t] = ca
    maxt = max(maxt, t)

dp=[[-10**18]*(10**5 + 1) for _ in range(5)]
dp[0][0] = 0

for t in range(1, maxt+1):
    for i in range(5):
        dp[i][t] = dp[i][t-1]
        if i!=0:
            dp[i][t] = max(dp[i][t], dp[i-1][t-1])
        if i!=4:
            dp[i][t] = max(dp[i][t], dp[i+1][t-1])
    dp[x[t]][t] += a[t];

print(max(dp[i][maxt] for i in range(5)))