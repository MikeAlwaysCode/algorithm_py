# import random
import sys

# import itertools
# import math
# import os
# from bisect import bisect, bisect_left
# from collections import *
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from io import BytesIO, IOBase
# from string import *

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
# from types import GeneratorType
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

'''
# Rabin-Karp rolling hash
# 1028 ms
MOD1 = 998244353
MOD2 = 10 ** 9 + 7

def solve() -> None:
    s = input()
    t = list(map(int, list(input())))
    k = sint()
    ans = set()
    b1 = 27
    b2 = 13331
    for i in range(len(s)):
        cnt = 0
        hash1 = hash2 = 0
        for j in range(i, len(s)):
            cnt += t[ord(s[j]) - 97] ^ 1
            if cnt > k: break
            # hash1 = (hash1 * b + (ord(s[j]) - 96)) % MOD1
            # hash2 = (hash2 * b + (ord(s[j]) - 96)) % MOD2
            hash1 = (hash1 * b1 + (ord(s[j]) - 96)) % MOD2
            hash2 = (hash2 * b2 + (ord(s[j]) - 96)) % MOD2
            ans.add((hash1, hash2))
    print(len(ans))
'''

'''
# Trie
# TLE
class TrieNode:
    def __init__(self, val):
        self.map = dict()

def solve() -> None:
    s = input()
    t = list(map(int, list(input())))
    k = sint()
    root = TrieNode(0)
    ans = 0
    for i in range(len(s)):
        cnt = 0
        node = root
        for j in range(i, len(s)):
            c = s[j]
            cnt += t[ord(c) - 97] ^ 1
            if cnt > k: break
            if c not in node.map:
                node.map[c] = TrieNode(0)
                ans += 1
            node = node.map[c]
    print(ans)
'''

def solve() -> None:
    s = input()
    t = list(map(int, list(input())))
    k = sint()
    subs = sorted(s[i:] for i in range(len(s)))
    ans = 0
    pre = ""
    for cur in subs:
        valid = False
        cnt = 0
        for i in range(len(cur)):
            cnt += t[ord(cur[i]) - 97] ^ 1
            if cnt > k: break
            if i >= len(pre) or cur[i] != pre[i]:
                valid = True
            if valid: ans += 1
        pre = cur
    print(ans)

solve()