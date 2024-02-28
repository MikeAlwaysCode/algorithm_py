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
    a, b, l = mint()
    s = set()
    i = 0
    while pow(a, i) <= l:
        pa, j = pow(a, i), 0
        while pa * pow(b, j) <= l:
            if l % (pa * pow(b, j)) == 0:
                s.add(l // (pa * pow(b, j)))
            j += 1
        i += 1
    print(len(s))


for _ in range(int(input())):
    solve()
