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
    n = int(input())
    s = input()
    
    cnt = collections.Counter()
    l = 0
    for r in range(1, n):
        if s[r] != s[r - 1]:
            cnt[s[l:r]] += 1
            l = r
    cnt[s[l:n]] += 1
    # print(cnt)
    ans = 0
    for k, v in cnt.items():
        if v > 1:
            ans = max(ans, len(k))
        else:
            ans = max(ans, len(k) - 1)
    print(ans)

t = int(input())
for _ in range(t):
    solve()