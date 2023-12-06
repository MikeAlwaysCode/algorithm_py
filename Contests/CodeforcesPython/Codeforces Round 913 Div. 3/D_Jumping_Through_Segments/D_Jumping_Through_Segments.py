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
    l = r = 0
    for _ in range(n):
        seg.append(tuple(mint()))
        r = max(r, seg[-1][1])

    def check(x: int) -> bool:
        fr = to = 0
        for left, right in seg:
            if to + x < left or fr - x > right:
                return False
            fr = max(fr - x, left)
            to = min(to + x, right)
        return True

    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(r)


for _ in range(int(input())):
    solve()
