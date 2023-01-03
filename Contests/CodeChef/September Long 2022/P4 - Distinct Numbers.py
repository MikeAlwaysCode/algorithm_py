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
    
    # 先求所有小于等于sqrt(n)的质数
    C = int(math.sqrt(n))

    isprime = [True] * (C + 1)
    primes = list()

    # 埃拉托斯特尼筛法
    for i in range(2, C + 1):
        if isprime[i]:
            primes.append(i)
        for j in range(i + i, C + 1, i):
            isprime[j] = False

    def calSum(a):
        return a * ( a ** k - 1) / (a - 1)
    
    for p in primes:
        if n % p == 0:
            kp = k // p

t = int(input())
for _ in range(t):
    solve()