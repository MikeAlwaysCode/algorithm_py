import collections
import itertools
import math
import random
import sys
from functools import *
from heapq import *
from string import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n, m, q = map(int, input().split())
    arr = ints()

    mx = (n + 1) * n // 2 * m

    def f(s: int):
        if s > mx:
            print(-1)
            return
        
        r = min(n, (int(math.sqrt(s * 8 + 1)) - 1) // 2)
        s -= (1 + r) * r // 2
        res = [1] * r
        for i in range(r, 0, -1):
            if s < i: continue
            cmx = (m - 1) * i
            if s >= cmx:
                s -= cmx
                res[i-1] = m
            else:
                l = s // i
                s -= l * i
                res[i-1] += l
            if s == 0:
                break

        print(1, r)
        print(*res)
    
    for a in arr:
        f(a)

solve()