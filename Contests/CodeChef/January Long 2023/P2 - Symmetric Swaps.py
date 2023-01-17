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
    A = ints()
    B = ints()

    mn, mx = 10 ** 9, 0
    mxx, mnn = 0, 10 ** 9
    for i in range(n):
        mn = min(mn, max(A[i], B[i]))
        mxx = max(mxx, max(A[i], B[i]))
        mx = max(mx, min(A[i], B[i]))
        mnn = min(mx, min(A[i], B[i]))

    print(min(abs(mn - mx), abs(mn - mxx), abs(mx - mnn)))

t = int(input())
for _ in range(t):
    solve()