import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    nums = ints()
    cnt = [0] * 20
    ans = s = 0
    for i in range(n - 1, -1, -1):
        s += n - 1 - i
        for bit in range(20):
            if (nums[i] >> bit) & 1:
                ans = (ans + (1 << bit) * (s - cnt[bit]) * (i + 1)) % MOD
                cnt[bit] = (cnt[bit] + (n - i)) % MOD
            else:
                ans = (ans + (1 << bit) * cnt[bit] * (i + 1)) % MOD
    print(ans * 2 % MOD)

solve()
