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
    edge = [-1] * (n + 1)
    edge[1] = 0
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
        edge[u] += 1
        edge[v] += 1

    cnt = 0
    q = int(input())
    for _ in range(q):
        qry = ints()
        if qry[0] == 1:
            if edge[qry[1]] == 0:
                cnt += 1
                edge[qry[1]] -= 1
                for x in tree[qry[1]]:
                    edge[x] -= 1
        else:
            if cnt == n:
                print(n - 1)
            elif cnt == n - 1:
                print(0)
            else:
                print(n - cnt - 1)

t = int(input())
for _ in range(t):
    solve()