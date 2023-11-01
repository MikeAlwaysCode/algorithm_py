import math
import sys
from bisect import *

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
    n, q = mint()
    nums = ints()
    x = ints()
    t = []
    p = []
    pres = math.inf
    for y in x:
        if y >= pres: continue
        t.append(y)
        p.append(pow(2, y - 1))
        pres = y
    t.reverse()
    p.reverse()
    for i in range(1, len(p)):
        p[i] += p[i - 1]
    # print(t)
    # print(p)
    for i, a in enumerate(nums):
        pw = 0
        while a % 2 == 0:
            pw += 1
            a //= 2
        j = bisect(t, pw)
        if j: nums[i] += p[j - 1]
    print(*nums)

for _ in range(int(input())):
    solve()