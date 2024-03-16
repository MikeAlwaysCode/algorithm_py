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
    s = []
    s.append(input())
    s.append(input())
    seen = [[False] * n for _ in range(2)]
    seen[0][0] = True
    for i in range(n):
        for j in range(2):
            if seen[j][i]:
                if i < n - 1 and s[j][i + 1] == '>':
                    if i < n - 2:
                        seen[j][i + 2] = True
                    else:
                        seen[j][i + 1] = True
                if s[j ^ 1][i] == '>':
                    if i < n - 1:
                        seen[j ^ 1][i + 1] = True
                    else:
                        seen[j ^ 1][i] = True
    print("YES" if seen[1][-1] else "NO")


for _ in range(int(input())):
    solve()
