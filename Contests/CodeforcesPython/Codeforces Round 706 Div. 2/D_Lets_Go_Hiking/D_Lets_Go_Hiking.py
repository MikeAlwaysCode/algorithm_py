import sys
from collections import *

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
    if n == 2:
        print(0)
        return
    mx = 0
    rg = [0] * n
    rl = [0] * n
    lg = [0] * n
    ll = [0] * n
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            ll[i] = ll[i - 1] + 1
        else:
            lg[i] = lg[i - 1] + 1
        mx = max(mx, ll[i], lg[i])
    for i in range(n - 2, -1, -1):
        if nums[i] > nums[i + 1]:
            rl[i] = rl[i + 1] + 1
        else:
            rg[i] = rg[i + 1] + 1
    cnt_gt = cnt_lt = 0
    for i in range(n):
        if lg[i] == mx and rg[i] == mx:
            print(0)
            return
        elif lg[i] == mx or rg[i] == mx:
            cnt_gt += 1
        if ll[i] == mx or rl[i] == mx:
            cnt_lt += 1
    if not mx & 1 and cnt_gt == 2 and cnt_lt == 1:
        print(1)
    else:
        print(0)


solve()
