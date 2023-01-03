def solve() -> None:
    n, m, x, y, d = map(int, input().split())

    if (x - d > 1 and y + d < m) or (x + d < n and y - d > 1):
        print(n + m - 2)
    else:
        print(-1)
    
    # if d * 2 + 1 >= n or d * 2 + 1 >= m or (x + d >= n and y + d >= m) or (x - d <= 1 and y - d <= 1):
    # if (x + d >= n and y + d >= m) or (x - d <= 1 and y - d <= 1):
    #     print(-1)
    # else:
    #     print(n + m - 2)

t = int(input())
for _ in range(t):
    solve()