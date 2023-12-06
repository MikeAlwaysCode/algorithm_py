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

col = "abcdefgh"

def solve() -> None:
    s = input()

    c, r = s[0], s[1]
    for i in range(1, 9):
        if i == int(r):
            continue
        print(c + str(i))
    for cs in col:
        if cs == c:
            continue
        print(cs + r)

for _ in range(int(input())):
    solve()