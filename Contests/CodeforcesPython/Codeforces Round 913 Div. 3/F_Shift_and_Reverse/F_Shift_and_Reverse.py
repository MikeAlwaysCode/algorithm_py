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
    ans = math.inf
    mn = nums[0]
    le = [1] * n
    ge = [1] * n
    for i in range(1, n):
        mn = min(mn, nums[i])
        if nums[i] >= nums[i - 1]:
            le[i] = le[i - 1] + 1
        if nums[i] <= nums[i - 1]:
            ge[i] = ge[i - 1] + 1
    if le[-1] == n:
        print(0)
        return
    if ge[-1] == n:
        print(1)
        return
    for i in range(n):
        if nums[i] == mn:
            if i == 0:
                if ge[-1] == n - 1:
                    ans = min(ans, 2)
            elif i == n - 1:
                if le[i - 1] == n - 1:
                    ans = min(ans, 1)
            else:
                if nums[0] >= nums[-1] and le[-1] >= n - i and le[i - 1] == i:
                    ans = min(ans, n - i, i + 2)
                if nums[0] <= nums[-1] and ge[i] == i + 1 and ge[-1] >= n - i - 1:
                    ans = min(ans, n - i, i + 2)
    print(-1 if ans == math.inf else ans)


for _ in range(int(input())):
    solve()
