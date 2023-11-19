import sys
from heapq import *

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
    n, m, k = mint()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, d = mint()
        u -= 1
        v -= 1
        g[u].append((v, d))
        g[v].append((u, d))
    
    ans = 0
    train = [-1] * n
    for _ in range(k):
        u, d = mint()
        u -= 1
        if train[u] == -1:
            train[u] = d
        else:
            ans += 1
            train[u] = min(train[u], d)
        
    
    print(ans)

solve()