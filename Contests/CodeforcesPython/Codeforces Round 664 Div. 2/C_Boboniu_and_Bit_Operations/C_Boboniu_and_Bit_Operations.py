import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n, m = map(int, input().split())
    A = ints()
    B = ints()
    
    bu = [[True] * len(B) for _ in range(len(A))]
    ans = 0
    for i in range(9, -1, -1):
        l = False
        for j, a in enumerate(A):
            chk = True
            for k, b in enumerate(B):
                if bu[j][k] and a & b & (1<<i) == 0:
                    chk = False
                    break
            l |= chk
        if l:
            ans |= 1 << i
        else:
            for j, a in enumerate(A):
                for k, b in enumerate(B):
                    if bu[j][k] and a & b & (1<<i) != 0:
                        bu[j][k] = False
    
    print(ans)
    '''
    for i in range(1 << 9):
        chka = True
        for a in A:
            chkb = False
            for b in B:
                if i | (a & b) == i:
                    chkb = True
                    break
            if not chkb:
                chka = False
                break
        if chka:
            print(i)
            return
    '''

# t = int(input())
t = 1
for _ in range(t):
    solve()