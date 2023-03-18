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

    if n < 3:
        print(-1)
        return
    
    ans = ['0'] * n
    for i in range(n - 1):
        ans[i] = '1'
        print("".join(ans))
        ans[i] = '0'
    
    print("1" * n)


for _ in range(int(input())):
# for _ in range(1):
    solve()