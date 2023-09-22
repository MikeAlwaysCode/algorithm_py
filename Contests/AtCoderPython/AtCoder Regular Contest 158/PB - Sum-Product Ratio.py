import sys

# import math
# from bisect import *
# from collections import *
# from functools import *
# from heapq import *
# from itertools import *
# from random import *
# from string import *
# from types import GeneratorType

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

def solve() -> None:
    n = sint()
    nums = ints()

    neg = [a for a in nums if a < 0]
    pos = [a for a in nums if a > 0]

    neg.sort(reverse = True)
    pos.sort(reverse = True)

    x = neg + pos

    def f(a, b, c):
        return (a + b + c) / (a * b * c)

    t1 = f(x[0], x[1], x[2])
    t2 = f(x[0], x[1], x[-1])
    t3 = f(x[0], x[-1], x[-2])
    t4 = f(x[-1], x[-2], x[-3])

    print(min(t1, t2, t3, t4))
    print(max(t1, t2, t3, t4))

solve()