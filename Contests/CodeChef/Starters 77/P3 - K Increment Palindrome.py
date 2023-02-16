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
    arr = ints()
    
    i, j = 0, n - 1
    s = mx = cnt = 0
    while i < j:
        cur = abs(arr[i] - arr[j])
        mx = max(mx, cur)
        s += cur
        cnt += (cur > 0)
        i += 1
        j -= 1

    if s == 0:
        print("YES")
    elif k == n:
        print("NO")
    elif k & 1 or n & 1:
        print("YES")
    else:
        # print("NO" if mx * 2 > s else "YES")
        # print("NO" if mx * 2 > s and (mx * 2 - s) & 1 and cnt > k else "YES")
        print("NO" if (s % k) & 1 else "YES")

t = int(input())
for _ in range(t):
    solve()