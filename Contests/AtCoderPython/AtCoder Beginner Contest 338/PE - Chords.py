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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    conn = []
    for _ in range(n):
        a, b = mint()
        if a > b:
            a, b = b, a
        conn.append((a, b))
    conn.sort()
    h = []
    for a, b in conn:
        while h and h[0] < a:
            heappop(h)
        if h and h[0] < b:
            print("Yes")
            return
        heappush(h, b)
    print("No")


solve()
