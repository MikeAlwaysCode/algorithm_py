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

class BinaryTrie:
    def __init__(self, max_bit: int = 30):
        self.inf = 1 << 63
        self.to = [[-1], [-1]]
        self.cnt = [0]
        self.max_bit = max_bit

    def add(self, num: int) -> None:
        cur = 0
        self.cnt[cur] += 1
        for k in range(self.max_bit, -1, -1):
            bit = (num >> k) & 1
            if self.to[bit][cur] == -1:
                self.to[bit][cur] = len(self.cnt)
                self.to[0].append(-1)
                self.to[1].append(-1)
                self.cnt.append(0)
            cur = self.to[bit][cur]
            self.cnt[cur] += 1

    def remove(self, num: int) -> bool:
        if self.cnt[0] == 0: return False
        cur = 0
        rm = [0]
        for k in range(self.max_bit, -1, -1):
            bit = (num >> k) & 1
            cur = self.to[bit][cur]
            if cur == -1 or self.cnt[cur] == 0: return False
            rm.append(cur)
        for cur in rm: self.cnt[cur] -= 1
        return True

    def count(self, num: int):
        cur = 0
        for k in range(self.max_bit, -1, -1):
            bit = (num >> k) & 1
            cur = self.to[bit][cur]
            if cur == -1 or self.cnt[cur] == 0: return 0
        return self.cnt[cur]

    # Get max result for constant x ^ element in array
    def max_xor(self, x: int) -> int:
        if self.cnt[0] == 0: return -self.inf
        res = cur = 0
        for k in range(self.max_bit, -1, -1):
            bit = (x >> k) & 1
            nxt = self.to[bit ^ 1][cur]
            if nxt == -1 or self.cnt[nxt] == 0:
                cur = self.to[bit][cur]
            else:
                cur = nxt
                res |= 1 << k
        return res

    # Get min result for constant x ^ element in array
    def min_xor(self, x: int) -> int:
        if self.cnt[0] == 0: return self.inf
        res = cur = 0
        for k in range(self.max_bit, -1, -1):
            bit = (x >> k) & 1
            nxt = self.to[bit][cur]
            if nxt == -1 or self.cnt[nxt] == 0:
                res |= 1 << k
                cur = self.to[bit ^ 1][cur]
            else:
                cur = nxt
        return res

def solve() -> None:
    n = int(input())
    vals = [0] + ints()
    tree = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    bt = BinaryTrie()
    ans = 0
    def dfs(x, p, xor, m):
        nonlocal ans
        bt.add(vals[x])
        xor ^= vals[x]
        c = len(tree[x])
        if x != 1: c -= 1
        if c == 0:  # is leaf
            ans += bt.max_xor(xor) * pow(m, MOD - 2, MOD) % MOD
        else:
            m = m * c % MOD
            for u in tree[x]:
                if u == p: continue
                dfs(u, x, xor, m)
        bt.remove(vals[x])
    dfs(1, 0, 0, 1)
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
        for u in tree[x]:
            if u == p: continue
            parent[u] = x
            q.append((xor ^ vals[u], u, x, m))
    '''
    print(ans % MOD)

sys.setrecursionlimit(500005)
t = int(input())
for _ in range(t):
    solve()