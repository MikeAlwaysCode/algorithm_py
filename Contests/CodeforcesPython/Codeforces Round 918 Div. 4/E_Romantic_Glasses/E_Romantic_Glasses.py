import sys
import random

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
    nums = ints()
    h = random.randint(1, 1 << 30)
    d = 0
    s = set([h])
    for i, x in enumerate(nums):
        if i & 1:
            d += x
        else:
            d -= x
        if d ^ h in s:
            print("YES")
            return
        s.add(d ^ h)
    print("NO")


for _ in range(int(input())):
    solve()
