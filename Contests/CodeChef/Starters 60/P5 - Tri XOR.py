import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    arr = ints()
    op = []

    # def add(ind: list[int]):
    #     x = 0
    #     while x in ind:
    #         x += 1
    #     ind.append(x)

    for bit in range(30):
        ind = []
        for i, a in enumerate(arr):
            if (a >> bit) & 1:
                ind.append(i)
        
        # print(ind)
        
        while len(ind) >= 3:
            x, y, z = ind.pop(), ind.pop(), ind.pop()
            A, B, C = arr[x] ^ arr[y], arr[y] ^ arr[z], arr[z] ^ arr[x]
            op.append((arr[x], arr[y], arr[z]))
            arr[x], arr[y], arr[z] = A, B, C
        
        if len(ind) == 0:
            continue

        while len(ind) < 3:
            # add(ind)
            # add(ind)
            
            x = 0
            while x in ind:
                x += 1
            ind.append(x)
            x += 1
            while x in ind:
                x += 1
            ind.append(x)

            x, y, z = ind.pop(), ind.pop(), ind.pop()
            # print(x, y, z)
            A, B, C = arr[x] ^ arr[y], arr[y] ^ arr[z], arr[z] ^ arr[x]
            op.append((arr[x], arr[y], arr[z]))
            arr[x], arr[y], arr[z] = A, B, C
            # print(arr)
            
            ind.append(y)
            ind.append(z)

        x, y, z = ind.pop(), ind.pop(), ind.pop()
        A, B, C = arr[x] ^ arr[y], arr[y] ^ arr[z], arr[z] ^ arr[x]
        op.append((arr[x], arr[y], arr[z]))
        arr[x], arr[y], arr[z] = A, B, C

        # print(arr)

    print(len(op))
    for x, y, z in op:
        print(x, y, z)
    # print(arr)

t = int(input())
for _ in range(t):
    solve()