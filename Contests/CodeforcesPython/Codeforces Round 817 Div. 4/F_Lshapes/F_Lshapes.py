def solve() -> None:
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    
    visit = [[False] * m for _ in range(n)]
    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    def star(i, j) -> bool:
        if 0 <= i < n and 0 <= j < m and grid[i][j] == '*':
            return True
        else:
            return False

    def check(i, j) -> bool:
        cnt = 0
        for dr, dc in dir:
            ni = i + dr
            nj = j + dc
            if star(ni, nj):
                cnt += 1
        return cnt == 2
    
    pair = [(0, 1, 1, 1), (1, 0, 1, 1), (0, 1, 1, 0), (1, -1, 1, 0), (-1, 1, 0, 1)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*' and not visit[i][j]:
                if not check(i, j):
                    print("No")
                    return
                chk = False
                for dr1, dc1, dr2, dc2 in pair:
                    ni1 = i + dr1
                    nj1 = j + dc1
                    ni2 = i + dr2
                    nj2 = j + dc2
                    
                    if star(ni1, nj1) and star(ni2, nj2) and check(ni1, nj1) and check(ni2, nj2):
                        visit[i][j] = visit[ni1][nj1] = visit[ni2][nj2] = True
                        chk = True
                        break
                if not chk:
                    # print(i, j, ni1, nj1, ni2, nj2)
                    print("No")
                    return
    print("Yes")

t = int(input())
for _ in range(t):
    solve()