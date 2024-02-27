import sys
from string import ascii_lowercase

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
    n = sint()
    s = input()
    trans = dict()
    for c in ascii_lowercase:
        trans[c] = c

    qry = []
    for _ in range(sint()):
        c, d = input().split()
        qry.append((c, d))
    
    for c, d in qry[::-1]:
        trans[c] = trans[d]

    ans = []
    for c in s:
        ans.append(trans[c])
    print("".join(ans))

solve()
