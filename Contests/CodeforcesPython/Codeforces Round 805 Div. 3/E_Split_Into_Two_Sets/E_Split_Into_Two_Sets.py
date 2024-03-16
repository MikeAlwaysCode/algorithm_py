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
    n = sint()
    g = [[] for _ in range(n)]
    for _ in range(n):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    
    if any(len(g[i]) != 2 for i in range(n)):
        print("NO")
        return
    
    for i in range(n):
        if not g[i]:
            continue
        cnt, u, pre = 0, i, -1
        while g[u]:
            cnt ^= 1
            u, pre = g[u][1] if g[u][0] == pre else g[u][0], u
            g[pre].clear()
        if cnt:
            print("NO")
            return
    print("YES")


for _ in range(int(input())):
    solve()
