import sys
from itertools import accumulate
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
    n, k = mint()
    nums = ints()

    def check(x) -> bool:
        left = [0] * (n + 1)
        h = []
        s = 0
        for i, a in enumerate(nums):
            if s + a <= x:
                s += a
                heappush(h, -a)
            elif h and -h[0] > a:
                s += a
                s += heappushpop(h, -a)
            left[i + 1] = len(h)
        
        h = []
        s = 0
        for i in range(n - 1, -1, -1):
            a = nums[i]
            if s + a <= x:
                s += a
                heappush(h, -a)
            elif h and -h[0] > a:
                s += a
                s += heappushpop(h, -a)
            if len(h) + left[i] >= k:
                return True
        return False

    pres = list(accumulate(sorted(nums), initial = 0))
    l, r = pres[(k + 1) // 2], pres[k] - pres[k // 2]
    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(r)

for _ in range(int(input())):
    solve()
