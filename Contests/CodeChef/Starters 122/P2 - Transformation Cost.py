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
    h = n.bit_length()
    lb = n & - n
    l = lb.bit_length()
    ans = 0
    for i in range(l, h):
        if not (n >> i) & 1:
            ans += lb
            lb = 1 << i
    print(ans)


for _ in range(sint()):
    solve()
