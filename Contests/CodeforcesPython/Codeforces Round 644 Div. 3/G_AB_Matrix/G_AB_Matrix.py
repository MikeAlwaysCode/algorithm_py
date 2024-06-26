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
    n, m, a, b = mint()
    if a * n != b * m:
        print("NO")
        return
    
    print("YES")
    shift = 1
    while shift * n % m:
        shift += 1
        
    j = 0
    for _ in range(n):
        if j + a <= m:
            print('0' * j + '1' * a + '0' * (m - j - a))
        else:
            print('1' * (j + a - m) + '0' * (m - a) + '1' * (m - j))
        j = (j + shift) % m

for _ in range(int(input())):
    solve()