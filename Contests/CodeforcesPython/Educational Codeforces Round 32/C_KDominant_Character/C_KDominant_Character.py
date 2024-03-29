import math
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
    s = input()
    pos = [-1] * 26
    mx = [0] * 26
    for i, c in enumerate(s):
        c = ord(c) - 97
        mx[c] = max(mx[c], i - pos[c])
        pos[c] = i
    n, ans = len(s), math.inf
    for i in range(26):
        if pos[i] == -1:
            continue
        mx[i] = max(mx[i], n - pos[i])
        ans = min(ans, mx[i])
    print(ans)


solve()
