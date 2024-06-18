import sys
from itertools import accumulate

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
    n, c = mint()
    nums = ints()
    nums[0] += c
    pres = list(accumulate(nums, initial=0))
    ans = [0] * n
    suff = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suff[i] = max(nums[i], suff[i + 1])
    mx = -1
    for i, x in enumerate(nums):
        if x <= mx or x < suff[i + 1]:
            ans[i] += i
            x += pres[i]
        if x < suff[i + 1]:
            ans[i] += 1
        mx = max(mx, nums[i])
    print(*ans)

for _ in range(int(input())):
    solve()