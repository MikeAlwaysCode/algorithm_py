import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def printQry(a) -> None:
    sa = str(a)
    # sb = str(b)
    print(f"? {sa}", flush = True)

def printAns(ans) -> None:
    # s = str(ans)
    s = " ".join(map(str, ans))
    print(f"! {s}", flush = True)

def solve() -> None:
    k = int(input())
    n = int(input())
    arr = ints()
    ans = [a % (k + 1) for a in arr]

    s = set(ans)
    d = dict()
    if len(s) < k:
        for a in s:
            printQry(a)
            f = int(input())
            d[a] = f
    else:
        tot = 0
        for a in range(k):
            printQry(a)
            f = int(input())
            d[a] = f
            tot += f
        d[k] = - tot

    for i in range(n):
        ans[i] = d[ans[i]]

    printAns(ans)

t = int(input())
for _ in range(t):
    solve()