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
    s = list(input())
    i = j = 0
    while j < len(s) and s[j] == s[i]:
        j += 1
    if j == len(s):
        print("NO")
    else:
        s[i], s[j] = s[j], s[i]
        print("YES")
        print("".join(s))


for _ in range(int(input())):
    solve()
