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
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, m = mint()
    s = input()
    t = input()
    pos = [[] for _ in range(26)]
    for i, c in enumerate(s):
        pos[ord(c) - 97].append(i)
    mx = [-1] * 26
    for c in t:
        d = ord(c) - 97
        if not pos[d]:
            print("NO")
            return
        l = max(mx[i] for i in range(d, 26))
        j = bisect(pos[d], l)
        if j == len(pos[d]):
            print("NO")
            return
        mx[d] = pos[d][j]
    print("YES")

for _ in range(int(input())):
    solve()