import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    s = input().strip()
    cnt0 = s.count("0")
    cnt1 = n - cnt0

    if cnt0 == 0 or cnt1 == 0:
        print(n, 0)
        return
    
    k = abs(cnt1 - cnt0)
    b = str(1 if cnt1 < cnt0 else 0)

    print(1, k + 1)
    while k > 0:
        cn = len(s)

        for i in range(cn - 1):
            if s[i] != s[i+1]:
                print(i+1, i+2, b)
                s = s[:i] + b + s[i+2:]
                k -= 1
                break

    cn = len(s)
    print(1, cn, b)
    '''
    if s.count('0') == n or s.count('1') == n:
        print(n, 0)
        continue
    
    dif = s.count('0') - s.count('1')
    print(1, abs(dif) + 1)
    while dif != 0:
        n = len(s)
        for i in range(n):
            if s[i] != s[i+1]:
                which = '0'
                if dif > 0:
                    which = '1'
                s = s[0:i] + which + s[i+2:]
                print(i+1, i+2, which)
                break
        dif = s.count('0') - s.count('1')
    n = len(s)
    print(1, n, 1)
    '''
t = int(input())
for _ in range(t):
    solve()