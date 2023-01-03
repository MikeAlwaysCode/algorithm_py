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
    n = int(input())
    arr = ints()
    
    l, r = 0, n
    ml, mr = 0, n
    for bit in range(31):
        cnt = 0
        s = e = -1
        for i in range(n):
            if (arr[i] >> bit) & 1:
                cnt += 1
                if s == -1:
                    s = i
                e = i + 1
        if cnt == 0:
            continue
        if cnt == 1:
            print(-1)
            return
        l = max(l, s)
        r = min(r, e)
        mn = l + 1
        mr = r - 1

    if l >= r:
        print(-1)
        return
    
    if l + 1 == r:
        print(1)
        return
    
    # print(max(n - l, r, r - ml + 1, mr - l + 1))
    print(max(n - l - 1, r - 1, r - l))

t = int(input())
for _ in range(t):
    solve()