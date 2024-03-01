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
    vals = ints()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    
    L, R = [-1] * n, [-1] * n
    depth = [-1] * n
    q = [0]
    depth[0] = t = 0
    while q:
        u = q[-1]
        if L[u] == -1:
            t += 1
            L[u] = t
            for v in g[u]:
                if depth[v] >= 0:
                    continue
                depth[v] = depth[u] + 1
                q.append(v)
        else:
            R[u] = t
            q.pop()

    bit = [[0] * (n + 1) for _ in range(2)]
    def query(t, x) -> int:
        res = 0
        while x:
            res += bit[t][x] - bit[t^1][x]
            x &= x - 1
        return res
    def add(t, x, v):
        while x <= n:
            bit[t][x] +=v
            x += x & -x

    for _ in range(m):
        qry = ints()
        if qry[0] == 1:
            u, v = qry[1] - 1, qry[2]
            add(depth[u] & 1, L[u], v)
            add(depth[u] & 1, R[u] + 1, -v)
        else:
            u = qry[1] - 1
            res = vals[u] + query(depth[u] & 1, L[u])
            print(res)

solve()
