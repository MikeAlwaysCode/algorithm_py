import math
import sys
from collections import deque
# from heapq import *
from itertools import accumulate

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
    n = sint()
    nums = ints()
    pres = list(accumulate(nums, initial=0))
 
    def check(x: int) -> bool:
        res = math.inf
        dp = [0] * (n + 1)
        q = deque([0])
        for i in range(n):
            while q and pres[i] - pres[q[0]] > x:
                q.popleft()
            dp[i + 1] = nums[i] + dp[q[0]]
            while q and dp[i + 1] <= dp[q[-1]]:
                q.pop()
            q.append(i + 1)
            if pres[-1] - pres[i + 1] <= x:
                res = min(res, dp[i + 1])
        '''
        dp = [math.inf] * n
        h = [(0, 0)]
        for i in range(n):
            while h and pres[i] - pres[h[0][1]] > x:
                heappop(h)
            dp[i] = nums[i] + h[0][0]
            heappush(h, (dp[i], i + 1))
            if pres[-1] - pres[i + 1] <= x:
                res = min(res, dp[i])
        '''
        return res <= x
    
    l, r = max(nums), sum(nums)
    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(r)


for _ in range(int(input())):
    solve()
