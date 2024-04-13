import math
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
    k = sint()
    idx = sorted(range(1, n + 1), key = lambda x: nums[x - 1])
    # print(idx)
    mn = math.inf
    ans = l = s = cur = 0
    for r, i in enumerate(idx):
        cur += (r - l) * nums[i - 1] - s
        s += nums[i - 1]
        if r - l == k:
            s -= nums[idx[l] - 1]
            cur -= s - nums[idx[l] - 1] * k
            l += 1
        if r - l == k - 1 and cur < mn:
            mn, ans = cur, l
    print(*idx[ans:ans + k])


solve()
