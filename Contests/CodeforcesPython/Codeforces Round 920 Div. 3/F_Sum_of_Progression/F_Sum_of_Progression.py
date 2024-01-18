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
    n, q = mint()
    nums = ints()

    B = math.isqrt(n)

    pres1 = [[0] * (n + B + 1) for _ in range(B + 1)]
    pres2 = [[0] * (n + B + 1) for _ in range(B + 1)]
    for d in range(1, B + 1):
        for i in range(n):
            pres1[d][i + d] = pres1[d][i] + nums[i]
            pres2[d][i + d] = pres2[d][i] + (i // d + 1) * nums[i]

    ans = [0] * q
    for i in range(q):
        s, d, k = mint()
        s -= 1
        if d <= B:
            r = s + d * k
            ans[i] = pres2[d][r] - pres2[d][s] - (pres1[d][r] - pres1[d][s]) * (s // d)
        else:
            for j in range(k):
                ans[i] += nums[s + j * d] * (j + 1)
 
    print(*ans)


for _ in range(int(input())):
    solve()
