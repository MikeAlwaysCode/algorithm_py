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
    
    cnt = collections.Counter([a % 3 for a in arr])

    a1, a2 = cnt[1], cnt[2]

    if a1 == a2:
        print(a1)
        return
    
    d = max(a1, a2) - min(a1, a2)
    if a1 and a2:
        print(d + max(a1, a2))
        
    if d <= 4:
        print(7 - d)
    else:
        print(1 + d - 4 + max(d - 2, 2))
    # ans = 3 * (d // 4) + (7 - (d % 4))
    # print(ans)

t = int(input())
for _ in range(t):
    solve()