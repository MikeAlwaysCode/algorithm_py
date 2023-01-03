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
    
    cnt = collections.Counter(arr)
    f = [0] * (n + 1)
    d = dict()

    ans = [0] * n
    curr = 1
    for i in range(n):
        if cnt[arr[i]] % arr[i] != 0:
            print(-1)
            return
        if arr[i] not in d:
            d[arr[i]] = curr
            curr += 1
        elif f[d[arr[i]]] >= arr[i]:
            d[arr[i]] = curr
            curr += 1
        ans[i] = d[arr[i]]
        f[d[arr[i]]] += 1
    
    print(*ans)

t = int(input())
for _ in range(t):
    solve()