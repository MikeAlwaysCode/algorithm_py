import collections
import itertools
import math
import random
import sys
from functools import *
from heapq import *
from string import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    
    if n & 1:
        print(-1)
        return
    
    ans = [n - (i - 1) // 2 * 2 - (i & 1) for i in range(1, n + 1)]
    print(*ans)

for _ in range(int(input())):
# for _ in range(1):
    solve()