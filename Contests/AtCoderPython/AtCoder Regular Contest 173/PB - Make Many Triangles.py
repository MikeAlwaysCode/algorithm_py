import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    x, y = [0] * n, [0] * n
    for i in range(n):
        x[i], y[i] = mint()

    mx = 0
    for i in range(n):
        for j in range(i + 1, n):
            cnt = 0
            for k in range(j + 1, n):
                if (y[j] - y[i]) * (x[k] - x[i]) == (y[k] - y[i]) * (x[j] - x[i]):
                    cnt += 1
            if cnt:
                mx = max(mx, cnt + 2)
    
    ans = min(n // 3, (n * 3 - mx * 3) // 3)
    print(ans)


solve()
