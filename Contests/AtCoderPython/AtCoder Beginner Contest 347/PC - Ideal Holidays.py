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
    n, a, b = mint()
    m = a + b
    s = set()
    nums = ints()
    for x in nums:
        s.add(x % m)
    d = sorted(s)
    for i, x in enumerate(d):
        r = (d[i - 1] - x) % m
        if r + 1 <= a:
            print("Yes")
            return
    print("No")


solve()
