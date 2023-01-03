def solve() -> None:
    n, m = map(int, input().split())
    arr = [[int(x) for x in input()] for i in range(n)]
    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # print(arr)
    ans = 0
    k = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                ans += 1
            elif k < 2:
                k = 1
                for d in dir:
                    ni = i + d[0]
                    nj = j + d[1]
                    if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                        k = 2
    print(ans - 2 + k)

t = int(input())
for _ in range(t):
    solve()