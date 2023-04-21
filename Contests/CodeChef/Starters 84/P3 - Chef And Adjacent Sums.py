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
    arr = ints()
    arr.sort()
    i, j = 0, n - 1
    while i < j and arr[j] == arr[-1]:
        if arr[i] == arr[-2]:
            print("NO")
            return
        i += 1
        j -= 1
    print("YES")

for _ in range(int(input())):
# for _ in range(1):
    solve()