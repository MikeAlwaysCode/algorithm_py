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

def getPrimes(n: int):
    primes = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            primes.append(d)
            while n % d == 0:
                n //= d
        if n == 1:
            break
        d += 1
    if n > 1:
        primes.append(n)
    return primes

def solve() -> None:
    a, b = map(int, input().split())

    # d = 2
    # while d * d <= b:
    #     if b % d == 0:
    #         if a % d != 0:
    #             print("No")
    #             return
    #         while b % d == 0:
    #             b //= d
    #     if b == 1:
    #         break
    #     d += 1
    # if b > 1:
    #     if a % b != 0:
    #         print("No")
    #         return
    # print("Yes")
    
    if a % b == 0:
        print("Yes")
        return

    g = math.gcd(a, b)
    while g > 1:
        if a % b == 0:
            print("Yes")
            return
        a, b = g, b // g
        g = math.gcd(a, b)
    print("No")


t = int(input())
for _ in range(t):
    solve()