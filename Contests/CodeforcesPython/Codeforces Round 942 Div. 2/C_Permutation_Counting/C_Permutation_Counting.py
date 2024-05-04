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
    nums.sort()
    i = s = 0
    while i < n and k >= nums[i] * i - s:
        s += nums[i]
        i += 1
    if i < n:
        d, m = divmod(s + k, i)
        ans = d * n - i + m + 1
    else:
        ans = s + k - n + 1
    print(ans)


for _ in range(int(input())):
    solve()
