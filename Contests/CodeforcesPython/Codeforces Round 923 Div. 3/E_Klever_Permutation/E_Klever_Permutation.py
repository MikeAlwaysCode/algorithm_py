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
    n, k = mint()
    d = [n, 1]
    ans = [0] * n
    for i in range(k):
        for j in range(i, n, k):
            ans[j] = d[i & 1]
            d[i & 1] += (i & 1) * 2 - 1
    print(*ans)


for _ in range(int(input())):
    solve()
