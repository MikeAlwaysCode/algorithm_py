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
    nums.sort()
    j = -1
    seen = [False] * n
    for i, x in enumerate(nums):
        if x % nums[0]:
            if j == -1:
                j = i
        else:
            seen[i] = True
    if j == -1:
        print("Yes")
        return
    for i in range(n):
        if seen[i]:
            continue
        if nums[i] % nums[j]:
            print("No")
            return
    print("Yes")


for _ in range(int(input())):
    solve()
