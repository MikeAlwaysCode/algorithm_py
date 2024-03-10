import sys
from collections import Counter

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

def to_mask(x: int) -> int:
    mask = 0
    for i, p in enumerate(primes):
        c = 0
        while x % p == 0:
            x //= p
            c += 1
            # mask ^= 1 << i
        mask |= (c & 1) << i
    return mask

def solve() -> None:
    n = sint()
    nums = ints()
    cnt = Counter()
    for x in nums:
        cnt[to_mask(x)] += 1

    pw2 = [1] * n
    for i in range(1, n):
        pw2[i] = pw2[i - 1] * 2 % MOD

    dp = [0] * (1 << len(primes))
    dp[0] = 1
    for k, v in cnt.items():
        ndp = [0] * (1 << len(primes))
        for mask, c in enumerate(dp):
            ndp[mask] = (ndp[mask] + c * pw2[v - 1]) % MOD
            ndp[mask ^ k] = (ndp[mask ^ k] + c * pw2[v - 1]) % MOD
        dp = ndp

    print((dp[0] - 1) % MOD)

solve()
