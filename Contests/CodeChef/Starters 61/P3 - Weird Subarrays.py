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
    # arr = ints() + [0]
    # ans = n
    # dl = al = 0
    # dsc = [0] * (n + 1)
    # for i in range(1, n + 1):
    #     if arr[i] < arr[i-1]:
    #         if al < i - 1:
    #             k = i - al + dsc[al]
    #             ans += k * (k - 1) // 2
    #         elif i == n:
    #             k = i - dl
    #             ans += k * (k - 1) // 2

    #         al = i
    #     elif arr[i] > arr[i-1]:
    #         dsc[i-1] = i - dl - 1
    #         dl = i
            
    # print(ans)
    left, right = [1]*n, [1]*n
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            left[i] += left[i-1]
        if arr[n-1-i] < arr[n-i]:
            right[n-1-i] += right[n-i]
    print(sum(left[i] * right[i] for i in range(n)))

t = int(input())
for _ in range(t):
    solve()