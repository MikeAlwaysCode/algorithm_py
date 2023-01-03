from itertools import accumulate
import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    A = ints()
    m = int(input())
    B = ints()

    ans = max(max(accumulate(A)), max(accumulate(A[::-1]))) + sum([b for b in B if b > 0])

    print(ans)

t = int(input())
for _ in range(t):
    solve()