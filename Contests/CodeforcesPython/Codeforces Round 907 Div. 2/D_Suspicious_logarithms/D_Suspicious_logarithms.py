import math
import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    l, r = mint()

    ans = 0
    x1 = l
    def getLog(x, y) -> int:
        res = int(math.log(x, y))
        while pow(y, res) > x:
            res -= 1
        return res
 
    while x1 <= r:
        y = getLog(x1, 2)
        z1 = getLog(x1, y)
        
        x2 = min(pow(2, y + 1) - 1, r)
        nxt = pow(y, z1 + 1)
        while nxt <= x2:
            ans = (ans + z1 * (nxt - x1)) % MOD
            x1, z1 = nxt, z1 + 1
            nxt *= y
        ans = (ans + z1 * (x2 - x1 + 1)) % MOD
        x1 = x2 + 1
    print(ans)

for _ in range(int(input())):
    solve()