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
    n, k = map(int, input().split())
    A = input().split()
    B = input().split()

    cnt1 = collections.Counter()
    cnt2 = collections.Counter()

    for s1, s2 in zip(A, B):
        if len(s1) != len(s2):
            print("NO")
            return
        cnt1.update(s1)
        cnt2.update(s2)
    
    cost = 0
    for key, v1 in cnt1.items():
        cost += abs(v1 - cnt2[key])
    
    if cost > k * 2:
        print("NO")
    else:
        print("YES")

for _ in range(int(input())):
# for _ in range(1):
    solve()