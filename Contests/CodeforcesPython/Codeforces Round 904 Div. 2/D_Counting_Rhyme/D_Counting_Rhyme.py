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
    n = sint()
    nums = ints()
    cnt = Counter(nums)
    dp = [0] * (n + 1)
    ans = n * (n - 1) // 2
    for i in range(1, n + 1):
        if cnt[i]:
            for j in range(i, n + 1, i):
                dp[j] = 1

    for i in range(1, n + 1):
        if dp[i] == 0: continue
        ci = dp[i]
        cc = 0
        for j in range(i, n + 1, i):
            dp[j] -= ci
            cc += cnt[j]
        ans -= ci * cc * (cc - 1) // 2

    print(ans)

for _ in range(int(input())):
    solve()