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
    g = []
    for _ in range(3):
        g.append(ints())
    
    edges = [[] for _ in range(n * 2 + 1)]
    
    def idx(x: int) -> int:
        return x if x > 0 else n - x
    
    def op(x: int) -> int:
        return n + x if x <= n else x - n

    for i in range(n):
        a, b, c = idx(g[0][i]), idx(g[1][i]), idx(g[2][i])
        oa, ob, oc = op(a), op(b), op(c)
        edges[oa].append(ob)
        edges[oa].append(oc)
        edges[ob].append(oa)
        edges[ob].append(oc)
        edges[oc].append(oa)
        edges[oc].append(ob)

    valid = [True] * (n * 2 + 1)
    seen = [False] * (n * 2 + 1)

    def bfs(x: int):
        seen[x] = True
        q = [x]
        s = {x}
        check = True
        while q:
            u = q.pop()
            for v in edges[u]:
                ov = op(v)
                if not valid[ov] or v in s:
                    check = False
                    break
                if seen[ov]:
                    continue
                seen[ov] = True
                s.add(ov)
                q.append(ov)
            if not check:
                break

        if not check:
            for u in s:
                valid[u] = False

    for i in range(1, n + 1):
        if valid[i] and not seen[i]:
            bfs(i)
        if valid[i + n] and not seen[i + n]:
            bfs(i + n)

    for i in range(1, n + 1):
        if not valid[i] and not valid[i + n]:
            print("NO")
            return

    print("YES")


for _ in range(int(input())):
    solve()
