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
    n, m, x = mint()
    z = [[False] * n for _ in range(2)]
    z[0][x - 1] = True
    cur = 0
    for _ in range(m):
        qry = input().split()
        d = int(qry[0])
        for i in range(n):
            if qry[1] == '0':
                z[cur ^ 1][i] = z[cur][(i - d) % n]
            elif qry[1] == '1':
                z[cur ^ 1][i] = z[cur][(i + d) % n]
            else:
                z[cur ^ 1][i] = z[cur][(i - d) % n] | z[cur][(i + d) % n]
        cur ^= 1
    ans = []
    for i in range(n):
        if z[cur][i]:
            ans.append(i + 1)
    print(len(ans))
    print(*ans)


for _ in range(int(input())):
    solve()
