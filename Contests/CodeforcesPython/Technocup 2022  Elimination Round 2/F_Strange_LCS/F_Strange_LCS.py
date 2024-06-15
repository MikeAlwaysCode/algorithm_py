import sys
from functools import cache

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
    pos = [[[] for _ in range(n)] for _ in range(123)]
    for i in range(n):
        pos[0][i].append(-1)
        s = input()
        for j, c in enumerate(s):
            pos[ord(c)][i].append(j)
    
    p = [[None] * (123) for _ in range(1 << n)]
    @cache
    def f(mask, c) -> int:
        # 97 - 122, 65 - 90
        fmask = fc = 0
        for nc in range(65, 123):
            if 90 < nc < 97:
                continue
            


for _ in range(int(input())):
    solve()
