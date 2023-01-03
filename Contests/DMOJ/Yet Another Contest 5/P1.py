import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, k, x = map(int, input().split())
    
    ans = [k-1] * n

    # pow2 = pow(2, n - 2)
    # y = (k - pow2) % k
    # z = (x - y) % k
    # for i in range(n-2):
    #     pow2 //= 2
    #     y = (y + pow2) % k
    #     z = (z - y) % k
    # z = (x - k * (n - 2) + pow(2, n - 1) - 1) % k
    # ans[n-1] = z
    ans[n-1] = (x + pow(2, n - 1) - 1) % k

    print(*ans)

# t = int(input())
# for _ in range(t):
solve()