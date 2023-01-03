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

MXBIT = 60

def solve() -> None:
    n, q = map(int, input().split())
    arr = ints()
    bit_pres = [[0] * (n + 1) for _ in range(MXBIT)]

    for i in range(n):
        for bit in range(MXBIT):
            bit_pres[bit][i+1] = bit_pres[bit][i] + ((arr[i] >> bit) & 1)
    # print(bit_pres)
    for _ in range(q):
        k, l1, r1, l2, r2 = map(int, input().split())
        cnt1 = bit_pres[k][r1] - bit_pres[k][l1-1]
        cnt2 = bit_pres[k][r2] - bit_pres[k][l2-1]

        print((r1-l1+1-cnt1) * cnt2 + cnt1 * (r2-l2+1-cnt2))

t = int(input())
for _ in range(t):
    solve()