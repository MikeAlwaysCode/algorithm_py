import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    arr = ints()
    vol = [0] * n

    fa = list(range(n+1))
    def find(x):
        # if fa[x] != x:
        #     fa[x] = find(fa[x])
        # return fa[x]
        cur = x
        while x != fa[x]:
            x = fa[x]
        if cur != x:
            fa[cur], cur = x, fa[x]
        return x

    m = int(input())
    q = []
    
    for _ in range(m):
        # q.append(list(map(int, input().split())))
        q.append(input())
        
    for i in range(m):
        query = list(map(int, q[i].split()))
        if query[0] == 1:
        # if len(query) == 3:
            p, x = query[1] - 1, query[2]
            p = find(p)

            while x and p < n:
                v = arr[p] - vol[p]
                if x > v:
                    x -= v
                    vol[p] = arr[p]
                    fa[p] = find(p+1)
                    p = find(p+1)
                else:
                    vol[p] += x
                    break
        else:
        # elif query[0] == 2:
        # elif len(query) == 2:
            k = query[1] - 1
            print(vol[k])


# t = int(input())
# for _ in range(t):
solve()