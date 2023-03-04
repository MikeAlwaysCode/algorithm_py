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
    x, y = map(int, input().split())

    if x == y:
        print("Chef" if x & 1 else "Chefina")
        return

    d = (abs(x - y) >= 2)
    if x > y:
        print("Chef" if y & 1 or d else "Chefina")
    else:
        print("Chef" if x & 1 and not d else "Chefina")

    
    


for _ in range(int(input())):
    solve()