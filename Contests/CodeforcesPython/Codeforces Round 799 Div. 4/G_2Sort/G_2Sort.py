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
    suff = 1
    ans = 0
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1] * 2:
            suff += 1
        else:
            suff = 1
        if suff > k:
            ans += 1
    print(ans)


for _ in range(int(input())):
    solve()
