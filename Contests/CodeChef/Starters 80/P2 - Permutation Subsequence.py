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
MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    arr = ints()
    
    cnt = collections.Counter(arr)
    ans = 0
    cur = pre = 1
    while True:
        if cnt[cur] == 0:
            break
        pre = pre * cnt[cur] % MOD
        ans = (ans + pre) % MOD
        cur += 1
    print(ans)


for _ in range(int(input())):
# for _ in range(1):
    solve()