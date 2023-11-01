import sys
from bisect import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    A = ints()

    a, b = [], []
    for x, y in zip(A[:n], A[n:]):
        while a and x < a[-1]:
            a.pop()
            b.pop()
        a.append(x)
        b.append(y)
    
    mn = min(b[:bisect(a, a[0])])
    if mn <= a[0]:
        print(a[0], mn)
        return
    
    l = bisect_left(a, b[0])
    r = bisect(a, b[0])
    print(*min(a[:l] + b[:l], a[:r] + b[:r]))

solve()