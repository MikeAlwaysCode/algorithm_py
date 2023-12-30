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
    idx = sorted(range(n), key = lambda x: nums[x])
    s = k = 0
    for i, j in enumerate(idx):
        if i >= k:
            s += nums[j]
            k += 1
        while k < n and s >= nums[idx[k]]:
            s += nums[idx[k]]
            k += 1
        ans[j] = k - 1
    print(*ans)


for _ in range(int(input())):
    solve()
