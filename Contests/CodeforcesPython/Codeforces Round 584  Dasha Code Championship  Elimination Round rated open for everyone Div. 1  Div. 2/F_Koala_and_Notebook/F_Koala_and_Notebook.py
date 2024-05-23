import math
import sys
from collections import deque

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, m = mint()
    g = [[] for _ in range(10 ** 6)]
    k = n
    def add(u, v, w):
        nonlocal k
        while w > 9:
            g[k].append((v, w % 10))
            w //= 10
            v = k
            k += 1
        g[u].append((v, w))
    for i in range(1, m + 1):
        u, v = mint()
        add(u - 1, v - 1, i)
        add(v - 1, u - 1, i)

    dis = [math.inf] * k
    dis[0] = 0
    q = deque([[0]])
    while q:
        cs = q.popleft()
        nxt = [[] for _ in range(10)]
        for u in cs:
            for v, w in g[u]:
                nxt[w].append((u, v))
        for w, es in enumerate(nxt):
            ns = []
            for u, v in es:
                if dis[v] != math.inf:
                    continue
                dis[v] = (dis[u] * 10 + w) % MOD
                ns.append(v)
            if ns:
                q.append(ns)
    
    print(*dis[1:n], sep = "\n")
    '''
    dis := make([]int, n)
	vis := make([]bool, n)
	vis[0] = true
	q := [][]int{{0}}
	for len(q) > 0 {
		vs := q[0]
		q = q[1:]
		type edge struct{ from, to int }
		nxt := [10][]edge{}
		for _, v := range vs {
			for _, e := range g[v] {
				nxt[e.wt] = append(nxt[e.wt], edge{v, e.to})
			}
		}
		for wt, es := range nxt {
			vs := []int{}
			for _, e := range es {
				w := e.to
				if !vis[w] {
					vis[w] = true
					dis[w] = (dis[e.from]*10 + wt) % 1_000_000_007
					vs = append(vs, w)
				}
			}
			if len(vs) > 0 {
				q = append(q, vs)
			}
		}
	}
    '''

solve()
