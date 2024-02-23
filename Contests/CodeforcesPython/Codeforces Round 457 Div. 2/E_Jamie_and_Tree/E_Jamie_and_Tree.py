import sys

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
    
def solve() -> None:
    n, m = mint()
    nums = ints()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    k = n.bit_length()
    tin = [-1] * n
    tout = [-1] * n
    parent = [[-1] * n for _ in range(k)]
    depth = [-1] * n
    depth[0] = t = 0

    # Cal dfs seq. and parent and depth
    q = [0]
    order = []
    while q:
        u = q[-1]
        if tin[u] == -1:
            order.append(u)
            t += 1
            tin[u] = t
            for v in g[u]:
                if depth[v] >= 0:continue
                depth[v] = depth[u] + 1
                parent[0][v] = u
                q.append(v)
        else:
            q.pop()
            tout[u] = t

    # Sum subtree value
    for u in order[::-1]:
        if parent[0][u] != -1:
            nums[parent[0][u]] += nums[u]
            
    for i in range(1, k):
        for j in range(n):
            if (p := parent[i - 1][j]) != -1:
                parent[i][j] = parent[i-1][p]

    # LCA Method
    def go_up(u, k):
        for i in range(k.bit_length()):
            if (k >> i) & 1:
                u = parent[i][u]
        return u

    def lca(u, v):
        d = depth[u] - depth[v]
        if d >= 0:
            u = go_up(u, d)
        else:
            v = go_up(v, -d)
        if u == v: return u
        for p in range(k-1, -1, -1):
            if parent[p][u] != parent[p][v]:
                u, v = parent[p][u], parent[p][v]
        return parent[0][u]

    # BIT for rmq
    bit1 = [0] * (n + 1)
    bit2 = [0] * (n + 1)

    def query(x: int) -> int:
        res, t = 0, x
        while x:
            # res += BITree[x]
            res += bit1[x] * t - bit2[x]
            x &= x - 1
        return res

    def add(x: int, val: int):
        t = x
        while x <= n:
            bit1[x] += val
            bit2[x] += val * (t - 1)
            x += x & -x

    root = 0

    for _ in range(m):
        qry = ints()
        if qry[0] == 1:
            root = qry[1] - 1
        elif qry[0] == 2:
            u, v, x = qry[1] - 1, qry[2] - 1, qry[3]
            anc = lca(u, v)
            if anc == root:
                add(1, x)
            elif not tin[anc] < tin[root] <= tout[anc]:
                add(tin[anc], x)
                add(tout[anc] + 1, -x)
            else:
                lu, lv = lca(u, root), lca(v, root)
                mxd = max(depth[lu], depth[lv])
                if mxd < depth[root]:
                    w = go_up(root, depth[root] - mxd - 1)
                    add(tin[w], -x)
                    add(tout[w] + 1, x)
                add(1, x)
        else:
            u = qry[1] - 1
            if u == root:
                print(nums[0] + query(n))
            elif not tin[u] < tin[root] <= tout[u]:
                print(nums[u] + query(tout[u]) - query(tin[u] - 1))
            else:
                w = go_up(root, depth[root] - depth[u] - 1)
                print(nums[0] + query(n) - nums[w] - query(tout[w]) + query(tin[w] - 1))

solve()
