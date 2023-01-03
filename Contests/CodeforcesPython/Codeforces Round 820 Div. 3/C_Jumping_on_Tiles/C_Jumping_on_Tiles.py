import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    s = input().strip()
    n = len(s)
    st, ed = ord(s[0]) - 97, ord(s[n-1]) - 97
    cost = abs(ed - st)
    v = [[] for _ in range(26)]
    for i, c in enumerate(s):
        v[ord(c) - 97].append(i + 1)

    ans = []
    step = 1 if ed >= st else -1
    while st != ed:
        ans.extend(v[st])
        st += step
    ans.extend(v[ed])
    '''
    idx = []
    st, ed = 0, 0
    for i, c in enumerate(s):
        idx.append((ord(c) - 96, i + 1))
        if i == 0:
            st = ord(c) - 96
        elif i == n - 1:
            ed = ord(c) - 96
    v = []
    cost = abs(ed - st)
    for p, i in idx:
        if i == 1 or i == n:
            continue
        if st <= p <= ed or ed <= p <= st:
            v.append([p, i])
    if st <= ed:
        v.sort()
    else:
        v.sort(reverse=True)
    
    if not v:
        print(cost, 2)
        print(1, n)
        return
    
    _, ans = zip(*v)

    ans = [1] + list(ans) + [n]
    '''
    print(cost, len(ans))
    print(*ans)

t = int(input())
for _ in range(t):
    solve()