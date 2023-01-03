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
    n, k = map(int, input().split())
    arr = ints()

    if n == 1 and arr[0] == k:
        print("Yes")
        return
    
    for i in range(n - 1):
        if arr[i] == k:
            print("Yes")
            return
    print("No")

t = int(input())
for _ in range(t):
    solve()