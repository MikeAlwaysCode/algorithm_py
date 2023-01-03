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
    s = input()

    if s != s[::-1]:
        print(1)
        print(2 * n)
        return
    
    cnt = s.count("1")
    if cnt == 2 * n or cnt == 0:
        print(-1)
        return

    if s[:n] != s[n-1::-1]:
        print(2)
        print(n, n)
    else:
        print(2)
        print(n + 1, n - 1)

t = int(input())
for _ in range(t):
    solve()