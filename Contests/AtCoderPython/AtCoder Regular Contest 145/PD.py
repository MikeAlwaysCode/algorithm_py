N, M = map(int, input().split())
xarr = list(map(int, input().split()))
# carr = [[int(_) for _ in input().split()] for i in range(M)]
carr = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    carr[a] = b

ans = 0
'''
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(0, N):
    for j in range(0, i+1):
        dp[i+1][0] = max(dp[i+1][0], dp[i][j])
        # print(i, j)
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + xarr[i] + carr[j+1])
        ans = max(ans, dp[i+1][j+1])
'''
'''
dp = [[0] * (N+2) for _ in range(2)]
op = 0
for i in range(1, N+1):
    dp[op][i] = -1
for i in range(1, N+1):
    print(dp)
    for j in range(N+1):
        if dp[op][j] != -1:
            # print(op^1)
            # print(j)
            dp[op^1][j+1] = max(dp[op^1][j+1], dp[op][j] + xarr[i-1])
            dp[op^1][0] = max(dp[op^1][0], dp[op][j])

    op ^= 1
    
    for j in range(N+1):
        if dp[op][j] != -1: dp[op][j] += carr[j];

for j in range(N+1): ans = max(ans, dp[op][j]);
print(dp)
print(ans)
'''
dp = [0] * (N+1)
for i in range(N+1):
  dp[i] = [0] * (N+1)
for i in range(1,N+1):
  dp[i][0] = max(dp[i-1])
  for j in range(1,i+1):
    dp[i][j] = dp[i-1][j-1] + xarr[i-1] + carr[j]  #表が出たとき
# print(dp)
print(max(dp[N]))
