import math
import sys
# from heapq import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, m = mint()
    msg = []
    for _ in range(n):
        msg.append(tuple(mint()))
    msg.sort(key=lambda x: (x[1], x[0]))
    ans = 0

    dp = [math.inf] * (n + 1)
    for i in range(n):
        for j in range(n, 0, -1):
            if j > 1:
                dp[j] = min(dp[j], dp[j - 1] + msg[i][0])
            else:
                dp[1] = min(dp[1], msg[i][0] - msg[i][1])
            if dp[j] + msg[i][1] <= m:
                ans = max(ans, j)

    '''
    # 贪心
    for i in range(n):
        if msg[i][0] > m:
            continue
        h = []
        s = 0
        for j in range(i, n):
            s += msg[j][0]
            left = m - msg[j][1] + msg[i][1]
            heappush(h, -msg[j][0])
            while h and left < s:
                s += heappop(h)
            ans = max(ans, len(h))
    '''

    print(ans)

for _ in range(int(input())):
    solve()
