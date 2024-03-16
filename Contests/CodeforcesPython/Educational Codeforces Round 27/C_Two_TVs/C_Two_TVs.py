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
    for _ in range(n):
        seg.append(tuple(mint()))
    seg.sort()
    pr1 = pr2 = -1
    for l, r in seg:
        if l <= pr1 and l <= pr2:
            print("NO")
            return
        elif l > pr1:
            pr1 = r
        else:
            pr2 = r
    print("YES")

solve()
