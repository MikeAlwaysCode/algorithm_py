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
    n, f, k = mint()
    nums = ints()
    gt = eq = 0
    for x in nums:
        if x > nums[f - 1]:
            gt += 1
        elif x == nums[f - 1]:
            eq += 1
    print("NO" if gt >= k else "YES" if gt + eq <= k else "MAYBE")


for _ in range(int(input())):
    solve()
