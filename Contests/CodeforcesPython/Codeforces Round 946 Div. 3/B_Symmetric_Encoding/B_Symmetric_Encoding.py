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
    n = sint()
    s = list(input())
    mp = sorted(set(s))
    d = dict()
    for i, c in enumerate(mp):
        d[c] = mp[len(mp) - 1 - i]
    for i, c in enumerate(s):
        s[i] = d[c]
    print("".join(s))


for _ in range(int(input())):
    solve()
