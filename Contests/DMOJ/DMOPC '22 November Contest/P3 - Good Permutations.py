import collections
import math
import random
import sys
from functools import reduce
from heapq import heapify, heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    arr = ints()

    isprime = [True] * (n + 1)
    fact = list(range(n + 1))
    for i in range(2, n + 1):
        if isprime[i]:
            for j in range(i + i, n + 1, i):
                fact[j] = i
                isprime[j] = False

    # d = dict()
    d = [0] * (n + 1)

    indgrees = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    for num in arr:
        tmp = num
        while tmp > 1:
            p = fact[tmp]
            # if p in d:
            if d[p]:
                indgrees[num] += 1
                graph[d[p]].append(num)
            d[p] = num
            while tmp % p == 0:
                tmp //= p
    
    h = [-i for i, v in enumerate(indgrees) if i > 0 and v == 0]
    # print(h)
    heapify(h)
    ans = []
    while h:
        ans.append(-heappop(h))
        for x in graph[ans[-1]]:
            indgrees[x] -= 1
            if indgrees[x] == 0:
                heappush(h, -x)

    print(*ans)

# t = int(input())
# for _ in range(t):
solve()