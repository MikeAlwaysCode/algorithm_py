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
    n, m = mint()
    nums = ints()
    nums.sort()
    cnt = [0] * (m + 1)
    ans = math.inf
    cur = j = 0
    for i in range(n):
        while j < n and cur < m - 1:
            x = nums[j]
            d = 1
            while d * d <= x:
                if x % d == 0:
                    if 2 <= d <= m:
                        cnt[d] += 1
                        if cnt[d] == 1:
                            cur += 1
                    if d * d != x and 2 <= x // d <= m:
                        cnt[x // d] += 1
                        if cnt[x // d] == 1:
                            cur += 1
                d += 1
            j += 1
        if cur == m - 1:
            ans = min(ans, nums[j - 1] - nums[i])
        else:
            break
        x = nums[i]
        d = 1
        while d * d <= x:
            if x % d == 0:
                if 2 <= d <= m:
                    cnt[d] -= 1
                    if cnt[d] == 0:
                        cur -= 1
                if d * d != x and 2 <= x // d <= m:
                    cnt[x // d] -= 1
                    if cnt[x // d] == 0:
                        cur -= 1
            d += 1
            
    print(-1 if ans == math.inf else ans)


for _ in range(int(input())):
    solve()
