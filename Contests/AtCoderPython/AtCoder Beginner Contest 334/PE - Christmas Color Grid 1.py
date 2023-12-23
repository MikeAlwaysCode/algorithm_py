import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, m = mint()
    g = []
    for _ in range(n):
        g.append(list(input()))

    fa = list(range(n * m + 1))

    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x

    def union(x: int, y: int):
        fa[find(x)] = find(y)

    ans = q = s = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == '.':
                q += 1
            else:
                s += 1
                curr = i * m + j
                if j and g[i][j - 1] == '#':
                    union(curr, i * m + j - 1)
                    curr = find(curr)
                    s -= 1
                if i and g[i - 1][j] == '#':
                    up = find((i - 1) * m + j)
                    if up != curr:
                        union(curr, up)
                        s -= 1

    # print(s)
    for i in range(n):
        for j in range(m):
            if g[i][j] == '#':
                continue
            cnt = set()
            for dr, dc in DIR:
                ni, nj = i + dr, j + dc
                if ni < 0 or ni >= n or nj < 0 or nj >= m or g[ni][nj] == '.':
                    continue
                cnt.add(find(ni * m + nj))
            if cnt:
                ans += s - len(cnt) + 1
            else:
                ans += s + 1

    print(ans * pow(q, MOD - 2, MOD) % MOD)


solve()
