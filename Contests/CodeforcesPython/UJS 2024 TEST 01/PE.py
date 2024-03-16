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
    n, m, q = mint()
    ball = ints()
    d = dict()
    qry = []
    for _ in range(q):
        qry.append(tuple(mint()))
    ans = [0] * n
    for op, u, v in qry[::-1]:
        if op == 1:
            if v in d:
                d[u] = d[v]
            else:
                d[u] = v
        elif not ans[u - 1]:
            if v in d:
                ans[u - 1] = d[v]
            else:
                ans[u - 1] = v
    for i, v in enumerate(ball):
        if not ans[i]:
            ans[i] = d[v] if v in d else v
            
    print(*ans)
    
solve()