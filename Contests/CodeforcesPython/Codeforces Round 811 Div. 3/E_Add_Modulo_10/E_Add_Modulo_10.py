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

def solve() -> None:
    n = sint()
    arr = ints()
    type1, type2, chk = False, False, True

    for i, a in enumerate(arr):
        if a % 5 == 0:
            type1 = True
            arr[i] += arr[i] % 10
            if i > 0 and arr[i] != arr[i-1]:
                chk = False
                break
        else:
            type2 = True
            while arr[i] % 10 != 2:
                arr[i] += arr[i] % 10
            if i > 0 and abs(arr[i] - arr[i-1]) % 20 != 0:
                chk = False
                break
        if type1 and type2:
            chk = False
            break
    
    print('Yes' if chk else 'No')

for _ in range(sint()):
    solve()