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
    n = sint()
    s = list(map(int, list(str(n))))
    i = 0
    while i < len(s) and s[i] != 0:
        i += 1
    if i == len(s):
        ans = 1 if s[-1] != 1 else 2
    else:
        ans = 1
        for j in range(i + 1, len(s)):
            ans *= 10
            if s[j] == 0:
                ans += 1
    print(ans)


for _ in range(sint()):
    solve()
