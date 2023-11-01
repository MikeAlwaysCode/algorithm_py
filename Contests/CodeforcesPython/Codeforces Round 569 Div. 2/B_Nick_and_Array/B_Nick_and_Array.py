import sys

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
    idx = 0
    nums = ints()
    for i, x in enumerate(nums):
        if x >= 0:
            nums[i] = - x - 1
        else:
            x = - x - 1
        if nums[i] < nums[idx]:
            idx = i
    if n & 1:
        nums[idx] = - nums[idx] - 1
    print(*nums)

solve()