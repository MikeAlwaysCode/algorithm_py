import sys
from collections import Counter

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
    n, k = mint()
    nums = ints()
    cnt = Counter()
    ans = 0
    for x in nums:
        primes = Counter()
        d = 2
        while d * d <= x:
            while x % d == 0:
                primes[d] += 1
                x //= d
            if x == 1:
                break
            d += 1
        if x > 1:
            primes[x] += 1
        curr = need = 1
        for p, v in primes.items():
            v %= k
            if v:
                curr *= pow(p, v)
                need *= pow(p, k - v)
        ans += cnt[need]
        cnt[curr] += 1
    print(ans)


solve()
