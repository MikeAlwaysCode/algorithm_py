import sys
from collections import deque

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

class TreeAncestor:
    def __init__(self, g: list):
        n = len(g)
        m = n.bit_length()

        size = [1] * n
        depth = [-1] * n
        depth[0] = 0
        pa = [[-1] * m for _ in range(n)]
        # BFS
        q = deque([0])
        s = []
        while q:
            u = q.popleft()
            s.append(u)
            for v in g[u]:
                if depth[v]>=0:continue
                depth[v] = depth[u] + 1
                pa[v][0] = u
                q.append(v)
        
        for u in s[::-1]:
            if (p := pa[u][0]) != -1:
                size[p] += size[u]

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]

        self.size = size
        self.depth = depth
        self.pa = pa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k >> i) & 1:  # k 二进制从低到高第 i 位是 1
                node = self.pa[node][i]
        return node

    # 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # 使 y 和 x 在同一深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # 同时上跳 2**i 步
        return self.pa[x][0]

def solve() -> None:
    n = sint()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    lca = TreeAncestor(g)

    for _ in range(sint()):
        u, v = mint()
        if u == v:
            print(n)
            continue
        u -= 1
        v -= 1

        if (lca.depth[u] + lca.depth[v]) & 1:
            print(0)
            continue

        anc = lca.get_lca(u, v)
        l = lca.depth[u] - lca.depth[anc]
        r = lca.depth[v] - lca.depth[anc]
        if l == r:
            ku = lca.get_kth_ancestor(u, l - 1)
            kv = lca.get_kth_ancestor(v, l - 1)
            print(n - lca.size[ku] - lca.size[kv])
        else:
            if l < r:
                u, v = v, u
                l, r = r, l
            m = (l + r) // 2
            ku = lca.get_kth_ancestor(u, m)
            ku0 = lca.get_kth_ancestor(u, m - 1)
            print(lca.size[ku] - lca.size[ku0])

solve()
