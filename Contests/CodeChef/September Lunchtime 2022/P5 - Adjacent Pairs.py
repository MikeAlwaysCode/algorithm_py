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

    oddCnt = collections.Counter([a for i, a in enumerate(arr) if i & 1])
    evenCnt = collections.Counter([a for i, a in enumerate(arr) if not i & 1])

    odd = list(oddCnt.items())
    even = list(evenCnt.items())

    odd.sort(key = lambda x: -x[1])
    even.sort(key = lambda x: -x[1])

    oddNum = (n + 1) // 2 
    evenNum = n // 2

    if odd[0][0] != even[0][0]:
        print(oddNum - odd[0][1] + evenNum - even[0][1])
    else:
        on = len(odd)
        en = len(even)
        if on == 1:
            on = oddNum
        else:
            on = oddNum - odd[1][1]
        if en == 1:
            en = evenNum
        else:
            en = evenNum - even[1][1]
        print(min(oddNum - odd[0][1] + en, (evenNum - even[0][1] + on)))

t = int(input())
for _ in range(t):
    solve()