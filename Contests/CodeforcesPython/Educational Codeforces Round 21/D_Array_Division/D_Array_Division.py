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
    n = sint()
    nums = ints()
    pres = list(accumulate(nums))
    if pres[-1] & 1:
        print("NO")
        return
    s = set()
    for i in range(n):
        if pres[i] * 2 == pres[-1]:
            print("YES")
            return
        if pres[i] * 2 > pres[-1] and pres[i] - pres[-1] // 2 in s:
            print("YES")
            return
        s.add(nums[i])
    s.clear()
    for i in range(n - 1, -1, -1):
        if pres[i] * 2 < pres[-1] and pres[-1] // 2 - pres[i] in s:
            print("YES")
            return
        s.add(nums[i])

    print("NO")


solve()
