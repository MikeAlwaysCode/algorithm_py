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
    i = 0
    while i < n and nums[i] == 0:
        i += 1
    if i == n:
        ans = [2] + [1] * (n - 1)
        print(*ans)
        return
    cnt, pre = 0, nums[i]
    last = -1
    for j in range(i + 1, n):
        if nums[j] != 0:
            cnt += abs(nums[j] - pre)
            if cnt > 1:
                print(-1)
                return
            pre = nums[j]
        else:
            last = j
            nums[j] = pre
    for j in range(i - 1, -1, -1):
        nums[j] = nums[i]
    if cnt == 0:
        if last == n - 1:
            nums[-1] = nums[i] + 1
        elif i:
            nums[0] = nums[i] + 1
        else:
            print(-1)
            return
    print(*nums)


solve()
