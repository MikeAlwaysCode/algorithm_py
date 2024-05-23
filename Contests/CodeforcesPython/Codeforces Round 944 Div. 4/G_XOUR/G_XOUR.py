import sys
from collections import defaultdict
from random import getrandbits

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
    h = getrandbits(31)
    pos = defaultdict(list)
    val = defaultdict(list)
    for i, x in enumerate(nums):
        mask = (x - (x & 3)) ^ h
        pos[mask].append(i)
        val[mask].append(x)
    for k, v in val.items():
        v.sort()
        for i, x in enumerate(v):
            nums[pos[k][i]] = x
    print(*nums)


for _ in range(int(input())):
    solve()
