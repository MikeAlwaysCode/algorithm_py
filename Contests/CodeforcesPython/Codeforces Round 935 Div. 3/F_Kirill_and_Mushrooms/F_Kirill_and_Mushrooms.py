import sys
from heapq import *

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
    v = ints()
    p = ints()
    ans = cnt = 0
    h = []
    for i in range(n - 1, -1, -1):
        heappush(h, v[p[i] - 1])
        while len(h) > i + 1:
            heappop(h)
        if len(h) == i + 1 and h[0] * (i + 1) >= ans:
            ans, cnt = h[0] * (i + 1), i + 1
    print(ans, cnt)


for _ in range(int(input())):
    solve()
