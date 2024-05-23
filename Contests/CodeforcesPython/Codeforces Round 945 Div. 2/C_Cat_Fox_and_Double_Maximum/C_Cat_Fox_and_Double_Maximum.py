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
    ans = [0] * n
    i = nums.index(1)
    i = i & 1
    idx = sorted(range(i, n, 2), key = lambda x: -nums[x])
    x = 1
    for j in idx:
        ans[j] = x
        x += 1
    i = (i + 1) & 1
    idx = sorted(range(i, n, 2), key = lambda x: nums[x])
    x = n
    for j in idx:
        ans[j] = x
        x -= 1
    print(*ans)


for _ in range(int(input())):
    solve()
