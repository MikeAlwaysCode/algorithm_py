import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce
from typing import Counter

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n = int(input())
    arr = ints()

    ans = [-1] * (n + 1)
    cnt = Counter(arr)
    pres = 0

    q = collections.deque()
    
    for i in range(n + 1):
        if i not in cnt:
            ans[i] = pres
            if not q:
                break
            else:
                j = q[-1]
                pres += i - j
                cnt[j] -= 1
                if cnt[j] == 1:
                    q.pop()
        else:
            ans[i] = pres + cnt[i]
            if cnt[i] > 1:
                q.append(i)

    print(*ans)

t = int(input())
for _ in range(t):
    solve()