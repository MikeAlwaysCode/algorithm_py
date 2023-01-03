import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    s1 = input()
    s2 = input()

    cnt = collections.Counter(s1) & collections.Counter(s2)

    print(0 if not cnt else cnt.most_common(1)[0][1])

t = int(input())
for _ in range(t):
    solve()