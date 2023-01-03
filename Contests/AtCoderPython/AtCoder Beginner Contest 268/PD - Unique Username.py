from itertools import permutations
import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, m = map(int, input().split())
    remain = 16 - n + 1
    s = []
    for _ in range(n):
        s.append(input().strip())
        remain -= len(s[-1])

    t = set()
    for _ in range(m):
        t.add(input().strip())

    def dfs(cur, ps, remain, ans):
        if remain < 0:
            return
        
        if cur == len(ps):
            if 3 <= len(ans) <= 16 and ans not in t:
                print(ans)
                exit()
            return

        if ans and ans[-1] != "_":
            dfs(cur, ps, remain, ans + "_")
        else:
            dfs(cur + 1, ps, remain, ans + ps[cur])
            if ans and remain > 0:
                dfs(cur, ps, remain - 1, ans + "_")

    for p in permutations(s):
        dfs(0, p, remain, "")

    print(-1)

# t = int(input())
# for _ in range(t):
solve()