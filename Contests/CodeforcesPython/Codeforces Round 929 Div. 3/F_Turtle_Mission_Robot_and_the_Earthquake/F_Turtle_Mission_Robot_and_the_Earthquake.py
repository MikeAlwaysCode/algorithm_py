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
    n, m = mint()
    g = []
    for _ in range(n):
        g.append(ints())
    ans = math.inf    
    q = [(0, 0)]
    seen = set()
    seen.add(0)
    step = 0
    while q:
        tmp = q
        q = []
        for x, y in tmp:
            if y == m - 1:
                ans = min(ans, step + x + 1, step + n - 1 - x)
            else:
                if g[(x + step + 1) % n][y] == 0 and g[(x + step + 2) % n][y] == 0 and ((x + 1) % n) * m + y not in seen:
                    q.append(((x + 1) % n, y))
                    seen.add(((x + 1) % n) * m + y)
                if g[(x + step + 1) % n][y + 1] == 0 and x * m + y + 1 not in seen:
                    q.append((x, y + 1))
                    seen.add(x * m + y + 1)
        step += 1
    print(-1 if ans == math.inf else ans)


for _ in range(int(input())):
    solve()
