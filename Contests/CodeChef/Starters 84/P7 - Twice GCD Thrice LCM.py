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

# region interactive
def printQry1(a, b) -> int:
    sa = str(a)
    sb = str(b)
    print(f"1 {sa} {sb}", flush = True)
    return int(input())
    
def printQry2(a, b, c) -> int:
    sa = str(a)
    sb = str(b)
    sc = str(c)
    print(f"2 {sa} {sb} {sc}", flush = True)
    return int(input())

def printAns(ans: list) -> None:
    s = " ".join(map(str, ans))
    print(f"3 {s}", flush = True)
# endregion interactive

def solve() -> None:
    n = int(input())
    ans = [0] * n
    i = 0
    while i + 3 < n:
        g12 = printQry1(i + 1, i + 2)
        g23 = printQry1(i + 2, i + 3)
        g34 = printQry1(i + 3, i + 4)
        g13 = printQry1(i + 1, i + 3)
        g24 = printQry1(i + 2, i + 4)
        g14 = printQry1(i + 1, i + 4)
        l123 = printQry2(i + 1, i + 2, i + 3)
        l234 = printQry2(i + 2, i + 3, i + 4)
        l134 = printQry2(i + 1, i + 3, i + 4)
        l124 = printQry2(i + 1, i + 2, i + 4)
        p123 = l123 * g12 * g23 * g13 // math.gcd(g12, g23, g13)
        p234 = l234 * g23 * g34 * g24 // math.gcd(g23, g34, g24)
        p134 = l134 * g13 * g34 * g14 // math.gcd(g13, g34, g14)
        p124 = l124 * g12 * g24 * g14 // math.gcd(g12, g24, g14)
        x = p124 * p134 * p123 // (p234 * p234)
        ans[i] = int(math.pow(x, 1/3))
        if ans[i] * ans[i] * ans[i] < x:
            ans[i] += 1
        x = p124 * p234 * p123 // (p134 * p134)
        ans[i + 1] = int(math.pow(x, 1/3))
        if ans[i + 1] * ans[i + 1] * ans[i + 1] < x:
            ans[i + 1] += 1
        x = p234 * p134 * p123 // (p124 * p124)
        ans[i + 2] = int(math.pow(x, 1/3))
        if ans[i + 2] * ans[i + 2] * ans[i + 2] < x:
            ans[i + 2] += 1
        x = p124 * p134 * p234 // (p123 * p123)
        ans[i + 3] = int(math.pow(x, 1/3))
        if ans[i + 3] * ans[i + 3] * ans[i + 3] < x:
            ans[i + 3] += 1
        i += 4
    
    while i < n:
        g45 = printQry1(i, i + 1)
        g35 = printQry1(i - 1, i + 1)
        l345 = printQry2(i - 1, i, i + 1)
        ans[i] = l345 * g34 * g45 * g35 // (math.gcd(g34, g45, g35) * ans[i - 1] * ans[i - 2])
        i += 1
        g34 = g45

    printAns(ans)
    res = int(input())
    if res == -1: exit(0)

for _ in range(int(input())):
    solve()