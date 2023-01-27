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
    s = input()

    i = 0
    while i < n and s[i] == '1':
        i += 1
    pre, ans, curr = i, 0, 0
    for a in s[i:]:
        if a == '0':
            ans = max(ans, curr)
            curr = 0
        else:
            curr += 1

    ans = max(ans, curr)
    print(pre + ans)

t = int(input())
for _ in range(t):
    solve()