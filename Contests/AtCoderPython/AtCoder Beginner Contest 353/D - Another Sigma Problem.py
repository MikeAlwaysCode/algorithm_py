import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    nums = ints()
    ans = 0
    p = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        p[i] = (p[i + 1] + pow(10, len(str(nums[i])), MOD)) % MOD
    for i, x in enumerate(nums):
        ans = (ans + x * p[i + 1] % MOD + x * i % MOD) % MOD
    print(ans)

solve()
