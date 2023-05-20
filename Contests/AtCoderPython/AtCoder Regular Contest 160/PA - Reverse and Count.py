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

class BIT:
    def __init__(self, n: int):
        self.nums = [0] * (n + 1)
        self.n = n
        self.BITree = [0] * (self.n + 1)
        
    def lowbit(self, x: int) -> int:
        return x & -x
    
    def query(self, x: int) -> int:
        ans = 0
        while x:
            ans += self.BITree[x]
            x -= self.lowbit(x)
        return ans

    def add(self, x: int, val: int):
        while x <= self.n:
            self.BITree[x] += val
            x += self.lowbit(x)

    def update(self, x: int, val: int) -> None:
        self.add(x + 1, val - self.nums[x])
        self.nums[x] = val

def solve() -> None:
    n, k = mint()
    arr = ints()

    if n == 1:
        print(arr)
        return
    
    m = arr[0] + n * (n - 1) // 2

    if k < arr[0]:
        j = arr.index(k)
        ans = arr[j::-1] + arr[j + 1:]
        print(*ans)
        return

    if k > m:
        j = arr.index(arr[0] + k - m)
        ans = arr[j::-1] + arr[j + 1:]
        print(*ans)
        return

    bit = BIT(n)
    for i in range(n - 1, -1, -1):
        l = bit.query(arr[i])
        r = 1 + (n - i) * (n - i - 1) // 2
        if k <= l:
            s = set(arr[i:])
            t = 1
            while k:
                if t not in s:
                    k -= 1
                t += 1
            j = arr.index(t)
            t = arr[i:j + 1]
            ans = arr[:i] + t[::-1] + arr[j + 1:]
            print(*ans)
            return

        k -= l - 1

        bit.update(arr[i], 1)

solve()