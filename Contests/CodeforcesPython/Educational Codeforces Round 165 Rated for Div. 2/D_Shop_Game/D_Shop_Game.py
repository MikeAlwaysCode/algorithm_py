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
    A = ints()
    B = ints()
    item = []
    ans = s = 0
    for a, b in zip(A, B):
        if a < b:
            s += b - a
            item.append((b, a))
    if len(item) <= k:
        print(0)
        return
    if k == 0:
        print(s)
        return
    item.sort(reverse=True)
    h = []
    for i in range(len(item)):
        s -= item[i][0]
        heappush(h, -item[i][1])
        if len(h) > k:
            s -= heappop(h)
        if len(h) == k:
            ans = max(ans, s)
    print(ans)


for _ in range(int(input())):
    solve()
