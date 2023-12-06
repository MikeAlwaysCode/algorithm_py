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
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    nums = ints()
    if n == 1:
        print(1)
        return
    nums.sort()
    ans = g = 0
    for i in range(1, n):
        g = math.gcd(g, nums[i] - nums[i - 1])
    for x in nums:
        ans += (nums[-1] - x) // g
    s = set(nums)
    k = n
    for i in range(1, n):
        if nums[-1] - i * g not in s:
            k = i
            break
    print(ans + k)

for _ in range(int(input())):
    solve()