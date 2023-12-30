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
    V = ints()
    T = ints()
    h = []
    ans = [0] * n
    s = 0
    for i, (v, t) in enumerate(zip(V, T)):
        heappush(h, s + v)
        while h and h[0] <= s + t:
            ans[i] += heappop(h) - s
        ans[i] += t * len(h)
        s += t
    print(*ans)
    

solve()
