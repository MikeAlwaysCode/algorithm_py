import sys
from bisect import bisect_left
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
    n = sint()
    nums = ints()
    pres = list(accumulate(nums, initial=0))
    ans = []
    for _ in range(sint()):
        l, u = mint()
        r = bisect_left(pres, pres[l - 1] + u)
        if r > n:
            ans.append(n)
        elif r == l or pres[r] == pres[l - 1] + u:
            ans.append(r)
        else:
            k = u - pres[r - 1] + pres[l - 1]
            s = (k + 1) * k // 2 - (nums[r - 1] - k - 1) * (nums[r - 1] - k) // 2
            if s > 0:
                ans.append(r)
            else:
                ans.append(r - 1)
    print(*ans)


for _ in range(int(input())):
    solve()
