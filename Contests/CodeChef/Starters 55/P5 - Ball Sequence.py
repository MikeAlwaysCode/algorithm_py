import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, k = map(int, input().split())
    arr = ints()
    
    ball = (arr[0] - 1) >> 1

    for i in range(1, k):
        ball += arr[i] - arr[i-1] - 1
        ball >>= 1
    ball += n - arr[-1]

    # print(n - k - ball.bit_count())
    print(n - k - bin(ball)[2::].count('1'))

t = int(input())
for _ in range(t):
    solve()