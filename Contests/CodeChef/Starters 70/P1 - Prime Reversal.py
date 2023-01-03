import collections
import math
import random
import sys
from functools import *
from heapq import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    sa = input()
    sb = input()

    if sa.count('1') == sb.count('1'):
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()