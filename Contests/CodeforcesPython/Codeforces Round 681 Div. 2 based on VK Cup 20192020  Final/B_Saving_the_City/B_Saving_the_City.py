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
    a, b = mint()
    s = input()
    ans, pre = 0, -1000
    for i, c in enumerate(s):
        if c == '1':
            ans += min(b * (i - pre - 1), a)
            pre = i
    print(ans)

for _ in range(int(input())):
    solve()