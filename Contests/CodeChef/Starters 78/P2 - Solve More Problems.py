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
    n, k = map(int, input().split())
    A = ints()
    B = ints()
    
    idx = sorted(range(n), key = lambda x: (A[x] + B[x], -A[x]))
    ans = mxb = 0
    for i in idx:
        if k >= A[i] + B[i]:
            ans += 1
            k -= A[i] + B[i]
            mxb = max(mxb, B[i])
        elif k >= A[i]:
            ans += 1
            break
        elif k >= A[i] + B[i] - mxb:
            ans += 1
            break
    print(ans)

t = int(input())
for _ in range(t):
    solve()