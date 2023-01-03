import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    arr = ints()

    g = 0
    for i in range(n-1):
        g = math.gcd(g, abs(arr[i] - arr[i+1]))
    
    print(2 if g == 1 else 1)
    '''
    arr.sort()

    cnt = set()
    for i in range(1, n):
        d = arr[i] - arr[i-1]
        if d == 1:
            print(2)
            return
        if d:
            cnt.add(d)
    
    if not cnt or len(cnt) == 1:
        print(1)
        return

    cnt = list(cnt)
    # cnt.sort()
    
    for i in range(1, len(cnt)):
        if math.gcd(cnt[i], cnt[i-1]) == 1:
            print(2)
            return
    print(1)
    
    # C = cnt[0]
    # isprime = [True] * (C + 1)
    # primes = []
    # # 埃拉托斯特尼筛法
    # for i in range(2, C + 1):
    #     if isprime[i] and C % i == 0:
    #         primes.append(i)
    #     for j in range(i + i, C + 1, i):
    #         isprime[j] = False
    
    # chk = False
    # s = set()
    # for p in primes:
    #     s.clear()
    #     chk = True
    #     for a in arr:
    #         s.add(a%p)
    #         if len(s) >= 2:
    #             chk = False
    #             break
    #     if chk:
    #         break

    # if chk:
    #     print(1)
    # else:
    #     print(2)
    '''

# t = int(input())
# for _ in range(t):
solve()