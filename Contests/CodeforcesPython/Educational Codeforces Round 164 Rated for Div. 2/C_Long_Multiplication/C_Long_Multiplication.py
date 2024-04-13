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
    x = list(map(int, list(input())))
    y = list(map(int, list(input())))
    n = len(x)
    i = 0
    while i < n and x[i] == y[i]:
        i += 1
    if i < n:
        if x[i] < y[i]:
            x[i], y[i] = y[i], x[i]
        for j in range(i + 1, n):
            if x[j] > y[j]:
                x[j], y[j] = y[j], x[j]
    print(*x, sep='')
    print(*y, sep='')


for _ in range(int(input())):
    solve()
