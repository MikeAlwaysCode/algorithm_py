def solve() -> None:
    n = int(input())
    # boxes = list()
    ans = 0
    x1 = x2 = y1 = y2 = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if x > 0:
            x1 = max(x1, x)
        elif x < 0:
            x2 = max(x2, abs(x))
        elif y > 0:
            y1 = max(y1, y)
        elif y < 0:
            y2 = max(y2, abs(y))

    ans += abs(x1) * 2 + abs(x2) * 2 + abs(y1) * 2 + abs(y2) * 2

    print(ans)

t = int(input())
for _ in range(t):
    solve()