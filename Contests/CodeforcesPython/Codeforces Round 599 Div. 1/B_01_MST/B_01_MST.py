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
    g = [set() for _ in range(n)]
    for _ in range(m):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].add(v)
        g[v].add(u)
    
    ans = 0
    s = set(range(n))
    for u in range(n):
        if u not in s:
            continue
        ans += 1
        s.remove(u)
        q = {u}
        while q:
            tmp = q
            q = set()
            for u in tmp:
                q |= s - g[u]
                s -= q
                if not s:
                    print(ans - 1)
                    return
            s -= q
        if not s:
            print(ans - 1)
            return
                        
    print(ans - 1)


solve()
