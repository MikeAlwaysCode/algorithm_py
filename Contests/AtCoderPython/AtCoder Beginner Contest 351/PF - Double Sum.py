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
    nums = ints()

    dis = {x:i for i, x in enumerate(sorted(set(nums)), 1)}
    tn = len(dis)
    bit = [[0] * 2 for _ in range(tn + 1)]

    def query(x: int):
        res = cnt = 0
        while x:
            cnt += bit[x][0]
            res += bit[x][1]
            x &= x - 1
        return (cnt, res)

    def add(x: int, val: int):
        while x <= tn:
            bit[x][0] += 1
            bit[x][1] += val
            x += x & -x

    ans = 0
    for x in nums:
        c, r = query(dis[x])
        ans += x * c - r
        add(dis[x], x)
    print(ans)

solve()
