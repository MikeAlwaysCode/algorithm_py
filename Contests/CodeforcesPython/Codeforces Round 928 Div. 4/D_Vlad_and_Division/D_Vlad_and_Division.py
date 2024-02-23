import sys
from collections import Counter
from random import randint, shuffle

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
    # h = randint(1, 1 << 31)
    shuffle(nums)
    # mx = (1 << 31) - 1
    cnt = Counter()
    ans = 0
    for x in nums:
        if cnt[x ^ 0x7fffffff]:
            cnt[x ^ 0x7fffffff] -= 1
        else:
            ans += 1
            cnt[x] += 1
        # if cnt[mx ^ x ^ h]:
        #     cnt[mx ^ x ^ h] -= 1
        # else:
        #     ans += 1
        #     cnt[x ^ h] += 1
    print(ans)

for _ in range(int(input())):
    solve()
