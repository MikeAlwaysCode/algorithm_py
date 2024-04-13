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
    nums = ints()

    def check(x: int) -> bool:
        a1 = a2 = 0
        for i in range(n - 1, -1, -1):
            if nums[i] + a2 < x:
                return False
            d = 0 if i < 2 else min(nums[i] + a2 - x, nums[i]) // 3
            a1, a2 = d * 2, a1 + d
        return True

    l, r = min(nums), max(nums)
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)


for _ in range(int(input())):
    solve()
