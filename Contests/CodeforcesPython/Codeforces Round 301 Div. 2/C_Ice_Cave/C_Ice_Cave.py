import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, m = mint()
    g = []
    for _ in range(n):
        g.append(input())
    sx, sy = mint()
    tx, ty = mint()

    sx -= 1
    sy -= 1
    tx -= 1
    ty -= 1

    cnt = 0
    for dr, dc in DIR4:
        nx, ny = tx + dr, ty + dc
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == '.':
            cnt += 1
    
    if tx == sx and ty == sy:
        print("YES" if cnt else "NO")
        return
    
    if cnt + (abs(tx - sx) + abs(ty - sy) == 1) <= (g[tx][ty] == '.'):
        print("NO")
        return
    
    q = [(sx, sy)]
    seen = [[False] * m for _ in range(n)]
    seen[sx][sy] = True
    while q:
        tmp = q
        q = []
        for x, y in tmp:
            for dr, dc in DIR4:
                nx, ny = x + dr, y + dc
                if not (0 <= nx < n and 0 <= ny < m) or seen[nx][ny]:
                    continue
                if nx == tx and ny == ty:
                    print("YES")
                    return
                if g[nx][ny] == '.':
                    seen[nx][ny] = True
                    q.append((nx, ny))
    print("NO")


solve()
