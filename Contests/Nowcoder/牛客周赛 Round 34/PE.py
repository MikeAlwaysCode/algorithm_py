import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    s = list(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    root = 0
    while root < n and s[root] == '?':
        root += 1
    if root == n:
        root = 0
        s[0] = 'p'
    t = 'dp'
    q = [(root, -1)]
    cur = t.index(s[root])
    while q:
        tmp = q
        q = []
        cur ^= 1
        for u, p in tmp:
            for v in g[u]:
                if v == p:
                    continue
                if s[v] == t[cur ^ 1]:
                    print(-1)
                    return
                if s[v] == '?':
                    s[v] = t[cur]
                q.append((v, u))
    print("".join(s))


solve()
