import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *
from types import GeneratorType

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

# # region interactive
# def printQry(a, b) -> None:
#     sa = str(a)
#     sb = str(b)
#     print(f"? {sa} {sb}", flush = True)

# def printAns(ans) -> None:
#     s = str(ans)
#     print(f"! {s}", flush = True)
# # endregion interactive

# # region dfsconvert
# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while True:
#                 if type(to) is GeneratorType:
#                     stack.append(to)
#                     to = next(to)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     to = stack[-1].send(to)
#             return to
#     return wrappedfunc
# # endregion dfsconvert

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

# mxn = 50_000
mxn = 32_000
factor = [1] * (mxn + 1)
primes = list()
def init():
    for i in range(2, mxn + 1):
        if factor[i] != 1:
            continue
        primes.append(i)
        for j in range(i, mxn + 1, i):
            factor[j] = i

def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 7, 61] if n < 1<<32 else [2, 3, 5, 7, 11, 13, 17] if n < 1<<48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    # L = [2, 3, 5, 7, 11, 13, 17]
    if n in L:
        return 1
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1: continue
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1: return 0
            t <<= 1
    return 1
 
def findFactorRho(n):
    from math import gcd
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g): return g
            elif isPrimeMR(n // g): return n // g
            return findFactorRho(g)
 
def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i*i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k: ret[i] = k
        i += 1 + i % 2
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k
 
    if n > 1: ret[n] = 1
    if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
    return ret

def solve() -> None:
    a, b, k = mint()

    mn = 0 if a == b else 1 if a % b == 0 or b % a == 0 else 2

    if k == mn:
        print("YES")
        return
    elif k < 2:
        print("NO")
        return
    
    def f(x: int) -> int:
        res = 0
        for p in primeFactor(x):
            while x % p == 0:
                res += 1
                x //= p
        return res
        '''
        res = 0
        for p in primes:
            if p * p > x: break
            while x % p == 0:
                res += 1
                x //= p
            if x == 1: break
        if x > 1: res += 1
        return res
        '''

    # g = math.gcd(a, b)
    # mx = f(g) * 2
    # if k <= mx:
    #     print("YES")
    #     return
    
    # mx += f(a // g)
    # if k <= mx:
    #     print("YES")
    #     return

    # mx += f(b // g)
    # if k <= mx:
    #     print("YES")
    # else:
    #     print("NO")

    # mx = f(a * b)
    mx = f(a) + f(b)
    print("YES" if k <= mx else "NO")

# init()
for _ in range(int(input())):
    solve()