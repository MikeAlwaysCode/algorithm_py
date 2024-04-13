import math
import sys
from heapq import *
from itertools import accumulate

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
    n, q = mint()
    A = ints()
    B = ints()
    pres = list(accumulate(A))
    for _ in range(q):
        k = sint()
        h = []
        ans = math.inf
        s = 0
        for i in range(n):
            heappush(h, -B[i])
            s += B[i]
            if len(h) > k:
                s += heappop(h)
            if len(h) >= k:
                ans = min(ans, pres[i] + s)
        print(ans)

solve()
