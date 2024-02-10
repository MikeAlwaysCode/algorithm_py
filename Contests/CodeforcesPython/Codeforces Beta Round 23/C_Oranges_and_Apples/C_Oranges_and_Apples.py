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
    n = sint()
    pair = []
    s = 0
    for i in range(n * 2 - 1):
        a, o = mint()
        s += o
        pair.append((a, o, i + 1))
    pair.sort()
    se = 0
    for i in range(0, n * 2 - 1, 2):
        se += pair[i][1]
    ans = []
    if se * 2 >= s:
        for i in range(0, n * 2 - 1, 2):
            ans.append(pair[i][2])
    else:
        for i in range(1, n * 2 - 1, 2):
            ans.append(pair[i][2])
        ans.append(pair[-1][2])

    print("YES")
    print(*ans)


for _ in range(int(input())):
    solve()
