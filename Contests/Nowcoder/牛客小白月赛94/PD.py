import math
import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    nums = ints()
    s = {nums[0]}
    p = 0
    for i in range(1, n):
        if nums[i] == 1:
            p = i
            break
        if nums[i] == nums[p]:
            nums[i] = nums[i - 1] + nums[p]
            while nums[i] in s:
                nums[i] += nums[p]
            if nums[i] > n:
                print(-1)
                return
        else:
            if math.gcd(nums[p], nums[i]) != nums[i]:
                print(-1)
                return
            p = i
        s.add(nums[i])
    i = 1
    while p < n:
        while i in s:
            i += 1
        nums[p] = i
        i += 1
        p += 1
    print(*nums)


solve()
