import sys
from heapq import *

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
    d = [0] * (n + 2)
    cats = []
    for _ in range(m):
        l, r = mint()
        d[l] += 1
        d[r + 1] -= 1
        cats.append((l, r))
    
    left = list(range(n + 1))
    cats.sort(key = lambda x: -x[1])
    i = 0
    h = []
    for j in range(n, 0, -1):
        while h and h[0] > j:
            heappop(h)
        while i < m and cats[i][1] >= j:
            heappush(h, cats[i][0])
            i += 1
        if h:
            left[j] = h[0]
    # print(left)
    dp = [0] * (n + 1)
    cur = 0
    for i in range(1, n + 1):
        cur += d[i]
        dp[i] = max(dp[i - 1], dp[left[i] - 1] + cur)
    print(dp[-1])


for _ in range(int(input())):
    solve()
