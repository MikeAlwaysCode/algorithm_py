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
    n = int(input())
    c = []
    for _ in range(n):
        c.append(ints()[1:])

    d = Counter()
    for i in range(n):
        for a in c[i]:
            d[a] += 1
        
    for i in range(n):
        chk = True
        for a in c[i]:
            if d[a] == 1:
                chk = False
        if chk:
            print("Yes")
            return

    print("No")

for _ in range(int(input())):
    solve()
