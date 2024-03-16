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
    if n <= 4:
        s = set(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] not in s:
                        print("NO")
                        return
        print("YES")
    else:
        nums.sort()
        if nums[0] + nums[-1] == 0 and nums[1] == nums[-2] == 0:
            print("YES")
        elif nums[0] == nums[-2] == 0 or nums[1] == nums[-1] == 0:
            print("YES")
        else:
            print("NO")

for _ in range(int(input())):
    solve()
