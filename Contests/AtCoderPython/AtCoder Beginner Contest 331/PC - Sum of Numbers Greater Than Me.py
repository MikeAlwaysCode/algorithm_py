import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    nums = ints()
    idx = sorted(range(n), key = lambda x: -nums[x])
    ans = [0] * n
    s = j = 0
    for i in idx:
        while j < n and nums[idx[j]] > nums[i]:
            s += nums[idx[j]]
            j += 1
        ans[i] = s
    print(*ans)

solve()