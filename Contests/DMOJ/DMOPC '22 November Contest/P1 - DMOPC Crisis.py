import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())

    # if n == 3:
    #     m = 1
    #     ans = "_M_"
    # elif n == 4:
    #     m = 2
    #     ans = "_MM_"
    # elif n == 5:
    #     m = 2
    #     ans = "_MM__"
    # elif n == 6:
    #     m = 2
    #     ans = "_MM___"

    m = n // 4 * 2 + (n % 4) // 3

    ans = "__MM" * (n // 4)

    ans += "__MM"[:n%4]

    print(m)
    print(ans)

# t = int(input())
# for _ in range(t):
solve()