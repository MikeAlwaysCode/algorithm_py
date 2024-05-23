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
    cnt1 = Counter()
    cnt2 = Counter()
    cnt3 = Counter()
    cnt4 = Counter()
    ans = 0
    for i in range(n - 2):
        ans += cnt1[(nums[i], nums[i + 1])] + cnt2[(nums[i], nums[i + 2])] + cnt3[(nums[i + 1], nums[i + 2])] - cnt4[(nums[i], nums[i + 1], nums[i + 2])] * 3
        cnt1[(nums[i], nums[i + 1])] += 1
        cnt2[(nums[i], nums[i + 2])] += 1
        cnt3[(nums[i + 1], nums[i + 2])] += 1
        cnt4[(nums[i], nums[i + 1], nums[i + 2])] += 1
    print(ans)


for _ in range(int(input())):
    solve()
