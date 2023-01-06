import collections
import math
import random
import sys
from functools import *
from heapq import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
MOD = 10 ** 9 + 7

HIGH_BIT = 30

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.sum = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, num: int, diff: int) -> None:
        cur = self.root
        for k in range(HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if not cur.children[bit]:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
            cur.sum += diff

    def get(self, num: int, x: int) -> int:
        res = 0
        cur = self.root
        for k in range(HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if (x >> k) & 1:
                if cur.children[bit]:
                    res += cur.children[bit].sum
                if not cur.children[bit ^ 1]:
                    return res
                cur = cur.children[bit ^ 1]
            else:
                if not cur.children[bit]:
                    return res
                cur = cur.children[bit]
        res += cur.sum
        return res

def solve() -> None:
    n = int(input())
    vals = [0] + ints()
    tree = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    ans = 0
    def dfs(x, p, xor, m):
        nonlocal ans

    '''
    parent = [0] * (n + 1)

    def cal(xor, x, m) -> int:
        p = 0
        while x != 0:
            p = max(p, xor ^ vals[x])
            x = parent[x]
        # print(p, m)
        return (p % MOD) * pow(m, MOD - 2, MOD) % MOD
        # return (p % MOD) * m % MOD

    q = collections.deque([(vals[1], 1, 0, 1)])
    while q:
        xor, x, p, m = q.popleft()
        c = len(tree[x])
        if x != 1: c -= 1
        if c == 0:  # is leaf
            ans += cal(xor, x, m)
            continue
        m *= c
        # m = m * pow(c, MOD - 2, MOD) % MOD
        for u in tree[x]:
            if u == p: continue
            parent[u] = x
            q.append((xor ^ vals[u], u, x, m))
    '''
    print(ans % MOD)

t = int(input())
for _ in range(t):
    solve()