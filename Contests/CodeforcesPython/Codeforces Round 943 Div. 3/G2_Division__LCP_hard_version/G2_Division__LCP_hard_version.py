import math
import sys
from functools import cache

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
    n, L, R = mint()
    s = input()
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    # print(z)

    @cache
    def check(x: int) -> int:
        cnt = 1
        i = x
        while i < n:
            if z[i] >= x:
                i += x
                cnt += 1
            else:
                i += 1
        return cnt
    
    def binary_search(k: int) -> int:
        l, r = 0, n // k
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid) >= k:
                l = mid
            else:
                r = mid - 1
        return l
    
    ans = [0] * (n + 1)

    for i in range(1, math.isqrt(n) + 1):
        ans[i] = binary_search(i)
    
    for x in range(1, math.isqrt(n) + 1):
        k = check(x)
        ans[k] = max(ans[k], x)

    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])

    print(*ans[L:R + 1])


for _ in range(int(input())):
    solve()
