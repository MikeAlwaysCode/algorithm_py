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

    # if n == 2:
    #     print(1, 1)
    #     return
    
    # a = int(math.sqrt(n))
    # if a * a == n:
    #     print(0, a)
    #     return

    if n % 4 == 3:
    # if n % 4 != 1:
        print(-1)
        return

    # def ran(n) -> int:
    #     while True:
    #         a = random.randint(1, n - 1)
    #         b = pow(a, (n - 1) // 4, n)
    #         if b * b % n == n - 1:
    #             return b if b <= (n - 1) // 2 else n - b

    # def cal(n):
    #     A = ran(n)
    #     B = 1
    #     # M = (A * A + B * B) // n
    #     s = A * A + B * B
    #     # while M > 1:
    #     while s != n:
    #         M = s // n
    #         u = A % M
    #         v = B % M
    #         if 2 * u > M:
    #             u = M - u
    #         if 2 * v > M:
    #             v = M - v
                
    #         A, B = (u * A + v * B) // M, (v * A - u * B) // M
    #         # M = (u * u + v * v) // M
    #         s = A * A + B * B
    #     print(abs(A), abs(B))

    # cal(n)

    pow2 = 0
    while not n & 1:
        n >>= 1
        pow2 += 1

    l = 0
    r = int(math.sqrt(n))
    while l <= r:
        tot = l * l + r * r
        if tot == n:
            for _ in range(pow2):
                l, r = r - l, l + r
            print(l, r)
            return
        elif tot < n:
            l += 1
        else:
            r -= 1
    print(-1)

t = int(input())
for _ in range(t):
    solve()