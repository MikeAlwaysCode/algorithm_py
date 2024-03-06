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
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    
    p = ints()

    tin = [-1] * n
    tout = [-1] * n
    q = [0]
    t = 0
    while q:
        u = q[-1]
        if tin[u] == -1:
            t += 1
            tin[u] = t
            for v in g[u]:
                if tin[v] != -1:
                    continue
                q.append(v)
        else:
            q.pop()
            t += 1
            tout[u] = t
            
    bit = [0] * (n * 2 + 1)
    
    def query(x: int):
        res = 0
        while x:
            res += bit[x]
            x &= x - 1
        return res
    
    def add(x: int, val: int):
        while x <= n * 2:
            bit[x] += val
            x += x & -x
    
    # 离线计算，注释参考：https://codeforces.com/contest/1899/submission/233583004
    qry = [[] for _ in range(n + 1)]
    for i in range(m):
        l, r, x = mint()
        qry[l - 1].append((x, i, -1))
        qry[r].append((x, i, 1))
    
    ans = [0] * m
    for i, a in enumerate(p, 1):
        add(tin[a - 1], 1)
        for x, j, t in qry[i]:
            ans[j] += t * (query(tout[x - 1]) - query(tin[x - 1] - 1))
    
    for a in ans:
        print("YES" if a else "NO")
    print()

for _ in range(int(input())):
    solve()