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

def solve() -> None:
    n, x, y = input().split()
    if x == y:
        print("Yes")
        return
    
    def clear_a() -> bool:
        j = 0
        for i in pos_a:
            while j < len(pos_cb) and pos_cb[j] < i:
                j += 1
            if j == len(pos_cb):
                return False
            j += 1
        return True
    
    n = int(n)
    pos_a, pos_ca, pos_cb = [], [], []
    for i, (a, b) in enumerate(zip(x, y)):
        if a != b:
            if b == 'C':
                print('No')
                return
            elif a == 'C':
                if b == 'B':
                    pos_ca.append(i)
                else:
                    pos_cb.append(i)
            elif a == 'A':
                pos_a.append(i)
            else:
                if pos_a:
                    pos_a.pop()
                elif pos_ca:
                    pos_ca.pop()
                else:
                    print("No")
                    return
        elif a == 'C':
            if not clear_a():
                print("No")
                return
            pos_a.clear()
            pos_ca.clear()
            pos_cb.clear()
        
    if not clear_a():
        print("No")
        return
                
    print("Yes")


for _ in range(sint()):
    solve()