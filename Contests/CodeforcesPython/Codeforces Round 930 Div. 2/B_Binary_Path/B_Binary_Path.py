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
    i = j = 0
    while i < n - 1 and (s[0][i + 1] == '0' or s[1][i] == '1'):
        if s[0][i + 1] == '0' and s[1][i] == '1':
            j = i + 1
        i += 1
    print(s[0][:i + 1] + s[1][i:])
    print(i - j + 1)
    
 
for _ in range(int(input())):
    solve()