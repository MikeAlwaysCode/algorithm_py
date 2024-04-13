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
    n, k = mint()
    nums = ints()
    k -= 1
    i = 0
    while i < n and nums[i] <= nums[k]:
        i += 1
    if i > k:
        print(i - 1)
        return
    j = i + 1
    while j < k and nums[j] <= nums[k]:
        j += 1
    print(max(i - 1, j - i - int(i == 0)))


for _ in range(int(input())):
    solve()
