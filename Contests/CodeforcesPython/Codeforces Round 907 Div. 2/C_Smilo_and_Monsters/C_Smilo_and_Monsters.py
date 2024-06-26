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
    ans = x = i = 0
    j = n - 1
    while i < j:
        x += nums[i]
        if x >= nums[j]:
            ans += nums[j] + 1
            x -= nums[j]
            j -= 1
        i += 1
    if i == j:
        x += nums[i]
    if x:
        ans += min(x, (x + 3) // 2)
    print(ans)

for _ in range(int(input())):
    solve()