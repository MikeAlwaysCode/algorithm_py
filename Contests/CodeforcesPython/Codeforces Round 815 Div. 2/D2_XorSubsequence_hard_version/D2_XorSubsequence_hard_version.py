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
B = 29
N = 200000 * (B + 1)
 
class BitTrie:
    def __init__(self):
        self.idx = 0
        self.trie = [[0] * N for _ in range(2)]
        self.dp = [[0] * N for _ in range(2)]
 
    def new_node(self):
        self.idx += 1
        self.trie[0][self.idx] = self.trie[1][self.idx] = 0
        self.dp[0][self.idx] = self.dp[1][self.idx] = 0
        return self.idx
 
bt = BitTrie()

def solve() -> None:
    n = sint()
    arr = ints()

    dp = [0] * n
    bt.idx = 0
    bt.new_node()
 
    for i, x in enumerate(arr):
        xi = x ^ i
        p = 1
        for j in range(B, -1, -1):
            v = xi >> j & 1
            t = bt.trie[v ^ 1][p]
            dp[i] = max(dp[i], bt.dp[i >> j & 1][t])
            p = bt.trie[v][p]
            if p == 0: break
        dp[i] += 1
        p = 1
        for j in range(B, -1, -1):
            v = xi >> j & 1
            t = bt.trie[v][p]
            if t == 0:
                bt.trie[v][p] = t = bt.new_node()
            p = t
            t = x >> j & 1
            bt.dp[t][p] = max(bt.dp[t][p], dp[i])
        
    print(max(dp))

for _ in range(int(input())):
    solve()