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
    arr = ints()
    absArr = list(map(abs, arr))
    arr.sort()
    absArr.sort()

    print(min(absArr[0] ** 2, arr[0] * arr[-1]), absArr[-1] ** 2)


t = int(input())
for _ in range(t):
    solve()