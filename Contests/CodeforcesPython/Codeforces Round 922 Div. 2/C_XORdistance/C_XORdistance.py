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
    a, b, r = mint()
    if a == b:
        print(0)
        return
    if a < b:
        a, b = b, a
    first = less = False
    for bit in range(60, -1, -1):
        op = False
        if (a >> bit) & 1 and not (b >> bit) & 1:
            if not first:
                first = True
            elif less or (r >> bit) & 1:
                op = True
        if op:
            a ^= 1 << bit
            b ^= 1 << bit
        if not less and (r >> bit) & 1 and not op:
            less = True
    print(a - b)


for _ in range(int(input())):
    solve()
