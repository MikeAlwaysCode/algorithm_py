import collections
import math
import random
import sys
from functools import *
from heapq import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n, m = map(int, input().split())
    sa = input()
    sb = input()
    cnta = collections.Counter(sa)
    cntb = collections.Counter(sb)

    if n >= m:
        cnta, cntb = cntb, cnta
        
    # print(cnta)
    # print(cntb)

    for ka, va in cnta.items():
        if cntb[ka] < va:
            print("NO")
            return
        cntb[ka] -= va
    
    single = 0
    for k, v in cntb.items():
        if v & 1:
            single += 1
            if single > 1:
                print("NO")
                return

    print("YES")

t = int(input())
for _ in range(t):
    solve()