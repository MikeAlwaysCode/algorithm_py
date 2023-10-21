import sys
from itertools import combinations

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
    ans = nums[0] | nums[-1]
    if n > 2:
        ans = max(nums[c[0]] | nums[c[1]] | nums[c[2]] for c in combinations(range(n), 3))
    else:
        ans = nums[0] | nums[-1]
    print(ans)


solve()