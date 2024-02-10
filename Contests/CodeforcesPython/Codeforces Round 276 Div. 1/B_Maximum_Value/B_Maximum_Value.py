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
    nums = sorted(set(ints()))
    last = [0] * (nums[-1] + 1)
    i = 0
    for j in range(1, nums[-1] + 1):
        if j == nums[i]:
            last[j] = j
            i += 1
        else:
            last[j] = last[j - 1]
    ans = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] <= ans:
            break
        for j in range(nums[i] * 2, nums[-1] + 1, nums[i]):
            ans = max(ans, last[j - 1] % nums[i])
        ans = max(ans, nums[-1] % nums[i])
    print(ans)

solve()
