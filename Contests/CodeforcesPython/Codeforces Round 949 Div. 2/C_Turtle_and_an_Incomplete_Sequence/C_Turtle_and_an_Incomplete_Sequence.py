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
    pos = []
    for i, x in enumerate(nums):
        if x != -1:
            pos.append(i)
    for i in range(1, len(pos)):
        l, r = pos[i - 1], pos[i]
        while l < r - 1 and nums[l] != nums[r]:
            if nums[l] > nums[r]:
                l += 1
                nums[l] = nums[l - 1] // 2
            else:
                r -= 1
                nums[r] = nums[r + 1] // 2
        if l == r - 1:
            if nums[l] != nums[r] // 2 and nums[r] != nums[l] // 2:
                print(-1)
                return
        elif (r - l) & 1:
            print(-1)
            return
        while l < r - 1:
            if nums[l] == nums[r]:
                nums[l + 1] = nums[l] * 2
            else:
                nums[l + 1] = nums[r]
            l += 1
    if not pos:
        pos.append(0)
        nums[0] = 1
    j = pos[0]
    while j:
        if nums[j] == nums[pos[0]]:
            nums[j - 1] = nums[j] * 2
        else:
            nums[j - 1] = nums[pos[0]]
        j -= 1
    j = pos[-1]
    while j < n - 1:
        if nums[j] == nums[pos[-1]]:
            nums[j + 1] = nums[j] * 2
        else:
            nums[j + 1] = nums[pos[-1]]
        j += 1
    print(*nums)



for _ in range(int(input())):
    solve()
