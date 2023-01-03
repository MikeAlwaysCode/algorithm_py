import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    arr = ints()
    cnt = sum(arr)
    
    print(min(cnt, n - cnt) + max(0, cnt * 2 - n) // 3)


t = int(input())
for _ in range(t):
    solve()