import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    # n = int(input())
    s = input()
    n = len(s)

    if n == 1:
        print(1)
    elif s[0] == s[-1]:
        print(n - 2)
    else:
        print(2)

    '''
    cnt01 = cnt10 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            continue
        if s[i] == '0':
            cnt10 += 1
        else:
            cnt01 += 1

    diff = cnt10 - cnt01
    if abs(diff) > 2:
        print(0)
        return
    
    ans = 0
    for i in range(n):
        cur = 0
        if i > 0:
            if s[i] == '0':
                cur -= 1
            else:
                cur += 1
        if i < n - 1:
            if s[i] == '0':
                cur += 1
            else:
                cur -= 1
        if diff + cur == 0:
            ans += 1
    print(ans)
    '''

t = int(input())
for _ in range(t):
    solve()