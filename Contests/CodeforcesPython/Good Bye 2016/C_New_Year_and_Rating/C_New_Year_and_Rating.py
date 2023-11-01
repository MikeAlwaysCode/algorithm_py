import sys
import math

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
    l, r = -math.inf, math.inf
    s = 0
    for _ in range(n):
        c, d = mint()
        if d == 1:
            l = max(l, 1900 - s)
        else:
            r = min(r, 1899 - s)
        
        s += c
    
    if l > r:
        print("Impossible")
    elif r == math.inf:
        print("Infinity")
    else:
        print(r + s)

solve()