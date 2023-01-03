import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    arr = ints()

    cnt = [0] * 31
    m = 0
    for i, a in enumerate(arr):
        m += (n - i) * (i + 1)
        for bit in range(31):
            cnt[bit] += ((a >> bit) & 1) * (n - i) * (i + 1)
    
    ans = 0
    for bit in range(31):
        ans += (cnt[bit] * 2 > m) << bit

    # print(m)
    # print(cnt)
    
    print(ans)

# t = int(input())
# for _ in range(t):
solve()