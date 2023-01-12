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
    n = int(input())
    arr = ints()

    def check(mask) -> bool:
        if (arr[0] & mask) != arr[0]: return False
        if (arr[-1] & mask) != arr[-1]: return False
        reach = arr[0]
        for i in range(1, n):
            if i > reach: return False
            if (arr[i] & mask) == arr[i]: reach = max(reach, i + arr[i])
        return True
        
    ans = 0
    for bit in reversed(range(21)):
        if check(ans + (1 << bit) - 1):
            continue
        else:
            ans += 1 << bit
    if check(ans):
        print(ans)
    else:
        print(-1)

t = int(input())
for _ in range(t):
    solve()