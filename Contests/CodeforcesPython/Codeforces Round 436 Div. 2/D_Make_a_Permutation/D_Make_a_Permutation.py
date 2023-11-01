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
    skip = [False] * (n + 1)
    ans = 0
    j = 1
    for i, x in enumerate(nums):
        if cnt[x] > 1:
            while cnt[j]:
                j += 1
            if j < x or skip[x]:
                cnt[x] -= 1
                nums[i] = j
                ans += 1
                j += 1
            else:
                skip[x] = True
    print(ans)
    print(*nums)

solve()