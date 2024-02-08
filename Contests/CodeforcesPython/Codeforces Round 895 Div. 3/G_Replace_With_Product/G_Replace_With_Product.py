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

    pos = list(i for i in range(n) if nums[i] > 1)
    
    if not pos:
        print(1, 1)
        return
    
    pres = list(accumulate(nums, initial = 0))
    s = 1
    for i in pos:
        s *= nums[i]
        # if s >= pres[-1]:
        # if s >= 1e10:
        if s >= n * 2:
            print(pos[0] + 1, pos[-1] + 1)
            return
    
    mx = 0
    l = r = 1
    for i in range(len(pos)):
        s = 1
        for j in range(i, -1, -1):
            s *= nums[pos[j]]
            if s - pres[pos[i] + 1] + pres[pos[j]] > mx:
                mx = s - pres[pos[i] + 1] + pres[pos[j]]
                l, r = pos[j] + 1, pos[i] + 1

    print(l, r)

for _ in range(int(input())):
    solve()
