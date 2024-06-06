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
    B = list(math.gcd(nums[i], nums[i + 1]) for i in range(n - 1))
    left = [1] * (n - 1)
    right = [1] * (n - 1)
    for i in range(1, n - 1):
        if B[i] >= B[i - 1]:
            left[i] = left[i - 1] + 1
    if left[-1] == n - 1 or left[-2] == n - 2:
        print("YES")
        return
    for i in range(n - 3, -1, -1):
        if B[i] <= B[i + 1]:
            right[i] = right[i + 1] + 1
    if right[1] == n - 2:
        print("YES")
        return
    for i in range(1, n - 1):
        x = math.gcd(nums[i - 1], nums[i + 1])
        if (i == 1 or x >= B[i - 2]) and (i == n - 2 or x <= B[i + 1]) and (i == 1 or left[i - 2] == i - 1) and (i == n - 2 or right[i + 1] == n - i - 2):
            print("YES")
            return
    print("NO")


for _ in range(int(input())):
    solve()
