import math
import sys
from collections import deque

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
    n, m, k, d = mint()
    cost = [0] * (n + 1)
    ans = math.inf
    for i in range(1, n + 1):
        nums = ints()
        h = deque([(1, 0)])
        for j in range(1, m):
            while h and h[0][1] < j - d - 1:
                h.popleft()
            cur = h[0][0] + nums[j] + 1
            while h and h[-1][0] >= cur:
                h.pop()
            h.append((cur, j))
        cost[i] = cost[i - 1] + h[-1][0]
        if i >= k:
            ans = min(ans, cost[i] - cost[i - k])
    print(ans)


for _ in range(int(input())):
    solve()
