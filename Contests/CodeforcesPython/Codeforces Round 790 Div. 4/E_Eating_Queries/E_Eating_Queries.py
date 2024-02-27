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
    n, q = mint()
    nums = ints()
    nums.sort(reverse=True)
    pres = list(accumulate(nums, initial=0))
    for _ in range(q):
        x = sint()
        if x > pres[-1]:
            print(-1)
        else:
            print(bisect_left(pres, x))


for _ in range(int(input())):
    solve()
