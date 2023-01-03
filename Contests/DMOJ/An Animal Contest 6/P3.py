import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = [0] * (n + 1)
    mx = 0
    mn = 101
    for i in range(n):
        cnt[i+1] = cnt[i] + arr[i]
        mx = max(mx, arr[i])
        mn = min(mn, arr[i])

    MD = n * 100

    ans = 0
    # d = [collections.defaultdict(int) for _ in range(101)]
    f = [0] * (MD * 2 + 1)
    for i in range(mn, mx+1):
        # d = collections.defaultdict(int)
        for j in range(0, n+1):
            p = cnt[j] - i * j
            f[p + MD] += 1
            ans += f[p + MD] - 1
        
        for j in range(0, n+1):
            p = cnt[j] - i * j
            f[p + MD] = 0
    '''
    f = [[0] * 2 for _ in range(MD * 2 + 1)]
    for i in range(mn, mx+1):
        for j in range(0, n+1):
            p = cnt[j] - i * j
            if f[p + MD][0] != i:
                f[p + MD][0] = i
                f[p + MD][1] = 1
            else:
                f[p + MD][1] += 1
                ans += f[p + MD][1] - 1
    '''
    print(ans)

# t = int(input())
# for _ in range(t):
solve()