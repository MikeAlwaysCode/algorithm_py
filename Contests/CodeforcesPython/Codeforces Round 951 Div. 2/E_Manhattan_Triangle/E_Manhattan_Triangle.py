import sys
from collections import Counter

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
    n, d = mint()
    s1 = Counter()
    s2 = Counter()
    for i in range(n):
        x, y = mint()
        s1[(x + y, x - y)] = i
    for k, v in s1.items():
        x, y = k
        r1, r2 = x + y, x - y
        
        if (r1 + d, r2) in s1 and (r1, r2 + d) in s1:
            print(v, s1[(r1 + d, r2)], s1[(r1, r2 + d)])
            return
    print(0, 0, 0)

for _ in range(int(input())):
    solve()
