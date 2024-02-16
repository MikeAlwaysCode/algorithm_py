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
    ans = 0
    xor = [0] * (n + 1)
    for i in range(n - 1):
        xor[i + 1] = xor[i] ^ nums[i]
    m = 0
    for i in range(n - 2, 0, -1):
        m |= nums[i]
        ans = max(ans, xor[i] + m + nums[-1])
    print(ans)

solve()
