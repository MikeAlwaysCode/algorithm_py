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
    n, k = mint()
    tb = []
    for i in range(n):
        tb.append(tuple(mint()))
    
    tb.sort(key = lambda x: -x[1])
    ans = s = 0
    h = []
    for i in range(n):
        if i < k:
            s += tb[i][0]
            heappush(h, tb[i][0])
        elif tb[i][0] > h[0]:
            s += tb[i][0] - h[0]
            heappushpop(h, tb[i][0])
        ans = max(ans, s * tb[i][1])
    
    print(ans)

solve()