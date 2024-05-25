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
    seg = []
    p = set()
    for _ in range(n):
        seg.append(tuple(mint()))
        p.add(seg[-1][0])
        p.add(seg[-1][1])
    seg.sort()

    dis = {x:i for i, x in enumerate(sorted(p), 1)}
    tn = len(dis)
    bit = [0] * (tn + 1)

    def query(x: int) -> int:
        res = 0
        while x:
            res += bit[x]
            x &= x - 1
        return res

    def add(x: int, val: int):
        while x <= tn:
            bit[x] += val
            x += x & -x

    ans = 0
    for i, (l, r) in enumerate(seg):
        ans += i - query(dis[l] - 1)
        add(dis[r], 1)
    print(ans)

solve()
