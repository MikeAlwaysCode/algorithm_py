import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    arr = ints()

    if n == 1 or arr[0] == arr[-1]:
        print("Yes")
        return

    for i in range(n - 1):
        if arr[i] == arr[0] and arr[i + 1] == arr[n - 1]:
            print("Yes")
            return

    print("No")


t = int(input())
for _ in range(t):
    solve()