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
    for i in range(n - 2):
        if nums[i + 2] < nums[i] or nums[i + 1] < nums[i] * 2:
            print("NO")
            return
        nums[i + 2] -= nums[i]
        nums[i + 1] -= nums[i] * 2
    print("YES" if nums[-1] == nums[-2] == 0 else "NO")


for _ in range(int(input())):
    solve()
