import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    dis = [0] * n
    # cnt = [0] * n
    # cnt = []
    # mx, mk = 0, 0
    for i, a in enumerate(arr):
        k = (i - a) % n
        dis[i] = k
        # cnt[k] += 1
        # if cnt[k] > mx:
        #     mx = cnt[k]
        #     mk = k
        # cnt.append(k)
    
    dis.sort()
    print(dis)
    ans = tot = sum(dis)
    pres = 0
    mid = n // 2
    mp = 0
    for i, d in enumerate(dis):
        pres += d
        if i < mid:
            mp += max(mid - d, 0)
        ct = tot - pres * 2 + ((i + 1) * 2 - n) * d
        # if i >= mid:
        #     ct -= 2
        ans = min(ans, ct)
    # print(mp)
    # # print(mk)
    # for k in cnt:
    #     cur = 0
    #     for i in range(n):
    #         cur += min((dis[i] - k)%n, (k - dis[i])%n)
    #     ans = min(ans, cur)
    print(ans)

# t = int(input())
# for _ in range(t):
solve()