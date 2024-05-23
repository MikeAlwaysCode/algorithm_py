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
    s = list(map(int, list(input())))
    ans = math.inf
    pos = [-1] * 3
    for i, c in enumerate(s):
        pos[c - 1] = i
        if min(pos) >= 0:
            ans = min(ans, i - min(pos) + 1)
    print(0 if ans == math.inf else ans)


for _ in range(int(input())):
    solve()
