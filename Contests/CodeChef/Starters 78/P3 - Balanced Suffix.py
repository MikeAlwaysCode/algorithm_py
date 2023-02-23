import collections
import math
import random
import sys
from functools import *
from heapq import *
from string import ascii_lowercase

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n, k = map(int, input().split())
    s = input()
    ss = sorted(set(s))
    cnt = collections.Counter(s)
    mn, mx = min(cnt.values()), max(cnt.values())
    if mx - mn > k:
        print(-1)
        return
    ans = [''] * n
    for i in range(n):
        for c in ss:
            if not cnt[c]: continue
            cnt[c] -= 1
            if max(cnt.values()) - min(cnt.values()) <= k:
                ans[i] = c
                break
            cnt[c] += 1
    print("".join(ans))

t = int(input())
for _ in range(t):
    solve()