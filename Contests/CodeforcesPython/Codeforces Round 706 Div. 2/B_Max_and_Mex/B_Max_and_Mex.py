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
    s = set(ints())
    if k == 0:
        print(n)
        return
    mx = max(s)
    mex = 0
    while mex in s:
        mex += 1
    if mex <= mx:
        s.add((mex + mx + 1) // 2)
        print(len(s))
    else:
        print(n + k)


for _ in range(int(input())):
    solve()
