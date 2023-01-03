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
    a, b = map(int, input().split())

    if b % a == 0 or a * 2 <= b:
        print("YES")
    else:
        print("NO")
    
    
    # (d, m) = divmod(b, a)

    # if m == 0:
    #     print("YES")
    #     return
    # for i in range(1, d):
    #     if (m + a * (d - 1 - i)) % i == 0:
    #         print("YES")
    #         return

    # print("NO")


t = int(input())
for _ in range(t):
    solve()