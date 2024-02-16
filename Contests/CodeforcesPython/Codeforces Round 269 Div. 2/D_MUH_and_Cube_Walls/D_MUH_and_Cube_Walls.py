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
    s = ints()
    if m == 1:
        print(n)
        return
    for i in range(m - 1):
        s[i] = s[i + 1] - s[i]
    s[-1] = math.inf
    for i in range(1, n):
        s.append(nums[i] - nums[i - 1])
    ans = 0
    pi = [0] * len(s)
    for i in range(1, len(s)):
        j = pi[i - 1]
        while j and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
        if pi[i] == m - 1:
            ans += 1
    print(ans)


solve()
