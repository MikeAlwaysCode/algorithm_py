import collections
import math
import random
import sys
from functools import *
from heapq import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n, k = map(int, input().split())
    s = input()

    if k == 1 and s[0] == '1':
        print(0)
        return
    
    ans = k
    curr = 0
    for i in range(1, n):
        if s[i] != s[i - 1]:
            curr += 1
        if i >= k and s[i - k] != s[i - k + 1]:
            curr -= 1
        if i >= k - 1:
            if s[i] == '1':
                ans = min(ans, curr)
            else:
                ans = min(ans, curr + 1)
    
    print(ans)


t = int(input())
for _ in range(t):
    solve()