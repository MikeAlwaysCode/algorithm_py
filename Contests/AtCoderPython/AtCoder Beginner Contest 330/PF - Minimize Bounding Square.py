import math
import sys
from bisect import *

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
    n, k = mint()
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = mint()
    if n == 1:
        print(0)
        return
    x.sort()
    y.sort()
    l, r = 0, max(x[-1] - x[0], y[-1] - y[0])
    if k == 0:
        print(r)
        return
    
    prex = [0] * (n + 1)
    prey = [0] * (n + 1)
    for i in range(n):
        prex[i + 1] = prex[i] + x[i]
        prey[i + 1] = prey[i] + y[i]

    sufx = [0] * (n + 1)
    sufy = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        sufx[i] = sufx[i + 1] + x[i]
        sufy[i] = sufy[i + 1] + y[i]
    
    def check(m: int) -> bool:
        cntx = cnty = math.inf
        for i, (a, b) in enumerate(zip(x, y)):
            j = bisect(x, a + m)
            cntx = min(cntx, a * i - prex[i] + sufx[j] - (n - j) * (a + m))
            j = bisect(y, b + m)
            cnty = min(cnty, b * i - prey[i] + sufy[j] - (n - j) * (b + m))
        
        for i in range(n - 1, -1, -1):
            a, b = x[i], y[i]
            rx = sufx[i] - (n - i) * a
            if a >= m:
                j = bisect(x, a - m)
                rx += (a - m) * j - prex[j]
            cntx = min(cntx, rx)
            ry = sufy[i] - (n - i) * b
            if b >= m:
                j = bisect(y, b - m)
                ry += (b - m) * j - prey[j]
            cnty = min(cnty, ry)

        return cntx + cnty <= k

    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(r)

solve()