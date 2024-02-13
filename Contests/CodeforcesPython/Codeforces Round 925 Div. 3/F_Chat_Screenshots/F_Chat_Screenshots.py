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
    n, k = mint()
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(k):
        arr = ints()
        for i in range(2, n):
            g[arr[i - 1] - 1].append(arr[i] - 1)
            deg[arr[i] - 1] += 1
    
    q = [i for i in range(n) if deg[i] == 0]
    while q:
        tmp = q
        q = []
        for u in tmp:
            for v in g[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)

    print("NO" if any(deg) else "YES")


for _ in range(int(input())):
    solve()
