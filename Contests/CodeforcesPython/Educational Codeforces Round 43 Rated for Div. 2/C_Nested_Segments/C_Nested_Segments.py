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
    seg = []
    for i in range(1, n + 1):
        l, r = mint()
        seg.append((l, r, i))
    seg.sort(key = lambda x: (x[0], -x[1]))
    for i in range(1, n):
        if seg[i][1] <= seg[i - 1][1]:
            print(seg[i][2], seg[i - 1][2])
            return
    print(-1, -1)
        


solve()
