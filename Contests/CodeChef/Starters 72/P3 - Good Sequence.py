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

    start = 0
    k = 1

    cs = -1
    ck = 1
    cnt = 0
    for i in range(n):
        if arr[i] == 1:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 1:
            if cs == -1:
                cs = i
            ck += 1
            cnt = 0
        elif cnt + ck <= 0:
            if ck > k:
                start = cs
                k = ck
            cs = -1
            ck = 1
            cnt = 0
    
    if ck > k:
        start = cs
        k = ck

    ans = [start + 1]
    cnt = 0
    for i in range(start, n):
        if arr[i] == 1:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 1:
            ans.append(i + 2)
            cnt = 0

    print(k)
    print(*ans)

t = int(input())
for _ in range(t):
    solve()