import sys
from collections import Counter
from heapq import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, q = mint()
    nums = ints()
    cnt = Counter(nums)
    h = []
    for i in range(n + 1):
        if cnt[i] == 0:
            heappush(h, i)
    for _ in range(q):
        i, x = mint()
        i -= 1
        cnt[nums[i]] -= 1
        if nums[i] <= n and cnt[nums[i]] == 0:
            heappush(h, nums[i])
        cnt[x] += 1
        nums[i] = x
        while h and cnt[h[0]]:
            heappop(h)
        print(h[0])

solve()