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
    n, k, s = map(int, input().split())
    ans = [0] * n
    i = 0
    while s:
        if i >= n:
            print(-2)
            return
            
        s, m = divmod(s, k)
        if m == 1:
            ans[i] = 1
        elif m == k - 1:
            ans[i] = -1
            s += 1
        elif m != 0:
            print(-2)
            return
        i += 1
    print(*ans)
    


t = int(input())
for _ in range(t):
    solve()