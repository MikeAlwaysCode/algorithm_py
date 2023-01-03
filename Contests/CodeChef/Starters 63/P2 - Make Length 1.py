import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    s = input()
    
    if n == 1:
        print("YES")
        return
    
    cnt = 0
    for c in s:
        if c == "1":
            cnt += 1
        else:
            if cnt & 1:
                print("NO")
                return
            cnt = 0
    
    if cnt & 1:
        print("NO")
    else:
        print("YES")


t = int(input())
for _ in range(t):
    solve()