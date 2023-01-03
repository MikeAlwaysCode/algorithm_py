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

    chk = True
    d = [0] * 2
    for i in range(1, n - 1):
        if arr[i] and ( arr[i-1] == arr[i] or arr[i] == arr[i+1]):
            chk = False
            break
        if arr[i-1] and arr[i] and arr[i+1]:
            if arr[i-1] < arr[i] > arr[i+1]:
                cur = 1
            elif arr[i-1] > arr[i] < arr[i+1]:
                cur = -1
            else:
                chk = False
                break

            if d[i&1] + cur == 0:
                chk = False
                break
            d[i&1] = cur

    print("YES" if chk else "NO")

t = int(input())
for _ in range(t):
    solve()