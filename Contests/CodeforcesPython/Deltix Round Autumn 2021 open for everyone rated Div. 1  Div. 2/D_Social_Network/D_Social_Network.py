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
    n, m = mint()

    fa = list(range(n))
    sz = [1] * n
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x
    
    more = 0
    cnt = [0] * (n + 1)
    cnt[1] = n
    
    for _ in range(m):
        x, y = mint()
        x -= 1
        y -= 1
        fx, fy = find(x), find(y)
        if fx == fy:
            more += 1
        else:
            cnt[sz[fx]] -= 1
            cnt[sz[fy]] -= 1
            sz[fy] += sz[fx]
            fa[fx] = fy
            cnt[sz[fy]] += 1
        
        ans = 0
        cur = more + 1
        for i in range(n, 0, -1):
            v = min(cur, cnt[i])
            ans += v * i
            cur -= v
            if cur == 0:
                break
        print(ans - 1)
        
    '''
    h = list((-1, i) for i in range(n))
    heapify(h)
    for _ in range(m):
        x, y = mint()
        x -= 1
        y -= 1
        fx, fy = find(x), find(y)
        if fx == fy:
            more += 1
        else:
            sz[fy] += sz[fx]
            fa[fx] = fy
            heappush(h, (-sz[fy], fy))
        
        ans = 0
        cur = []
        while len(cur) < more + 1:
            s, u = heappop(h)
            if s != -sz[u] or u != find(u):
                continue
            ans -= s
            cur.append(u)
        for u in cur:
            heappush(h, (-sz[u], u))
        print(ans - 1)
    '''

solve()
