import random
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
    ans = 0
    h = random.randint(1, 1 << 30)
    cnt = Counter()
    for x in nums:
        if x == 1 or x == 2:
            ans += cnt[1]
            cnt[1] += 1
        else:
            ans += cnt[x ^ h]
            cnt[x ^ h] += 1
    print(ans)

for _ in range(int(input())):
    solve()