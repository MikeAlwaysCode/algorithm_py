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
    n, l, r = mint()
    nums = ints()
    nums.sort()
    j1 = j2 = n - 1
    ans = 0
    for i in range(n):
        while j2 > i and nums[i] + nums[j2] > r:
            j2 -= 1
        if j2 <= i:
            break
        j1 = max(j1, i)
        while j1 > i and nums[i] + nums[j1] >= l:
            j1 -= 1
        ans += j2 - j1
    print(ans)


for _ in range(int(input())):
    solve()
