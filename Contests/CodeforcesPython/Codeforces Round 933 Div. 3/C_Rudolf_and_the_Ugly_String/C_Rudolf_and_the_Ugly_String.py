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
    ans = 0
    for i in range(2, n):
        if s[i - 2] == 'm' and s[i - 1] == 'a' and s[i] == 'p':
            ans += 1
        elif i >= 4 and s[i - 4] == 'm' and s[i - 3] == 'a' and s[i - 2] == 'p' and s[i - 1] == 'i' and s[i] == 'e':
            continue
        elif s[i - 2] == 'p' and s[i - 1] == 'i' and s[i] == 'e':
            ans += 1
    print(ans)


for _ in range(int(input())):
    solve()
