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
    ans = i = 0
    while i < n and nums[i] == 0:
        i += 1
    j = n - 1
    while j > i and nums[j] == 0:
        j -= 1
    while i < j:
        if nums[i] == 0:
            ans += 1
        i += 1
    print(ans)


for _ in range(int(input())):
    solve()
