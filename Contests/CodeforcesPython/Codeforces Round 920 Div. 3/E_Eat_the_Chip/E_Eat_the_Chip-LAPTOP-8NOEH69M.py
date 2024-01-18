import sys
from collections import deque

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
    h, w, xa, ya, xb, yb = mint()
    if xa >= xb:
        print("Draw")
        return
    d = xb - xa
    if d & 1:
        # Alice
        x = d // 2
        if yb - ya > 1 and min(w, yb + x) > ya + x + 1:
            print("Draw")
        elif ya - yb > 1 and max(1, yb - x) < ya - x - 1:
            print("Draw")
        else:
            print("Alice")
    else:
        # Bob
        x = d // 2
        if ya > yb and min(w, ya + x) > yb + x:
            print("Draw")
        elif ya < yb and max(1, ya - x) < yb - x:
            print("Draw")
        else:
            print("Bob")

for _ in range(int(input())):
    solve()