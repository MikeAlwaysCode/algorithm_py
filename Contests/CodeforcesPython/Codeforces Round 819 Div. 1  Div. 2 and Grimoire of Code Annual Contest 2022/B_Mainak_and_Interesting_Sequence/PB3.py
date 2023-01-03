import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce
input = sys.stdin.readline
 
ints = lambda: list(map(int, input().split()))

t = int(input())
for _ in range(t):
    n, m = ints()
    if m < n:
        print("NO")
    elif n % 2 == 1:
        res = [1] * (n - 1)
        res.append(m - (n - 1))
        print("YES")
        print(" ".join([str(x) for x in res]))
    elif n % 2 == 0:
        if m % 2 == 1:
            print("NO")
        else:
            res = [1] * (n - 2)
            res.append((m - (n - 2))//2)
            res.append(res[-1])
            print("YES")
            print(" ".join([str(x) for x in res]))