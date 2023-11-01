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
    n, s, l = mint()
    nums = ints()
    mx = deque()
    mn = deque()
    dp = [math.inf] * (n + 1)
    dx = set()
    dm = set()
    dp[0] = 0
    j = 0
    for i, x in enumerate(nums):
        while mx and nums[mx[-1]] < x:
            dx.add(mx.pop())
        while mn and nums[mn[-1]] > x:
            dm.add(mn.pop())
        mn.append(i)
        mx.append(i)
        while nums[mx[0]] - nums[mn[0]] > s:
            if mx[0] < mn[0]:
                dx.add(mx.popleft())
            elif mx[0] > mn[0]:
                dm.add(mn.popleft())
        while j in dm and j in dx or (nums[j] < nums[mn[0]] or nums[j] > nums[mx[0]]):
            j += 1
        if i - j + 1 >= l:
            dp[i + 1] = dp[j] + 1
    # print(dp)
    print(-1 if dp[n] == math.inf else dp[n])

solve()