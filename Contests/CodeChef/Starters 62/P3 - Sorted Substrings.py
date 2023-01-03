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

    print(s.count("10"))
    
    # cnt1 = s.count("1")
    # if cnt1 == n or cnt1 == 0:
    #     print(0)
    #     return

    # ans = 0
    # for i in range(n-1):
    #     if s[i] == '1' and s[i+1] == '0':
    #         ans += 1

    # print(ans)

t = int(input())
for _ in range(t):
    solve()