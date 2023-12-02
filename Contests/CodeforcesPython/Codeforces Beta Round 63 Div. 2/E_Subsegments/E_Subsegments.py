import random
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
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, k = mint()
    hx = random.randint(1, 1 << 30)
    cnt = Counter()
    h = []
    nums = []
    for i in range(n):
        nums.append(sint())
        cnt[nums[-1] ^ hx] += 1
        if cnt[nums[-1] ^ hx] == 1:
            heappush(h, -nums[-1])
        if i >= k:
            cnt[nums[i - k] ^ hx] -= 1
            if cnt[nums[i - k] ^ hx] == 1:
                heappush(h, -nums[i - k])
        if i >= k - 1:
            while h and cnt[(-h[0]) ^ hx] != 1:
                heappop(h)
            print(-h[0] if h else "Nothing")

solve()