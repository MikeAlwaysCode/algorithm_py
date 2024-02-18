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
    s = input()
    ans = i = 0
    while i < n:
        if s[i] == '@':
            ans += 1
        if i < n - 1 and s[i + 1] != '*':
            i += 1
        elif i < n - 2 and s[i + 2] != '*':
            i += 2
        else:
            break
    print(ans)


for _ in range(int(input())):
    solve()
