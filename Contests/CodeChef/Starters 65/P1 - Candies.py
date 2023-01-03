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

def solve() -> None:
    n = int(input())
    arr = ints()
    
    cnt = collections.Counter(arr)
    if cnt.most_common(1)[0][1] > 2:
        print("No")
    else:
        print("Yes")

t = int(input())
for _ in range(t):
    solve()