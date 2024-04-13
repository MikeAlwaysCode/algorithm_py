import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    s = input().upper()
    t = input()
    seen1 = set()
    seen2 = set()
    for c in s:
        if c == t[2] and t[:2] in seen2:
            print("Yes")
            return
        for a in seen1:
            seen2.add(a + c)
            if t[2] == 'X' and t[:2] == a + c:
                print("Yes")
                return
        seen1.add(c)
    print("No")

solve()
