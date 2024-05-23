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
    r = sint()

    def f(d: int) -> int:
        res = 0
        for x in range(d):
            m = d * d - x * x
            y = math.isqrt(m)
            if y == 0:
                break
            res += y if y * y < m else y - 1
        return res * 4 + 1
    
    print(f(r + 1) - f(r))

for _ in range(int(input())):
    solve()
