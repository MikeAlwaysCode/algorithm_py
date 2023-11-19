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
    ans = -math.inf
    odd = even = -math.inf
    for x in nums:
        if x & 1:
            odd = max(even + x, x)
            even = -math.inf
            ans = max(ans, odd)
        else:
            even = max(odd + x, x)
            odd = -math.inf
            ans = max(ans, even)
    print(ans)


for _ in range(int(input())):
    solve()