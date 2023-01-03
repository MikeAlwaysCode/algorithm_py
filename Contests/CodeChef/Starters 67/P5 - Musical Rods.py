import collections
import functools
# from itertools import accumulate
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7


def solve() -> None:
    n = int(input())
    A = ints()
    B = ints()

    def comp(x, y):
        return A[y] * B[x] - A[x] * B[y]

    ind = [i for i in range(n)]
    ind.sort(key = functools.cmp_to_key(comp))
    # print(ind)
    ans = prv = 0
    for i in ind:
        ans += B[i] * prv
        prv += A[i]

    print(ans)

t = int(input())
for _ in range(t):
    solve()