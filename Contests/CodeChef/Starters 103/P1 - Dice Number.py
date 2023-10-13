import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *
from types import GeneratorType

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    nums = ints()
    A = sorted(nums[:3])
    B = sorted(nums[3:])
    s1 = sum(x * (10 ** i) for i, x in enumerate(A))
    s2 = sum(x * (10 ** i) for i, x in enumerate(B))
    print("Alice" if s1 > s2 else "Tie" if s1 == s2 else "Bob")

for _ in range(int(input())):
    solve()