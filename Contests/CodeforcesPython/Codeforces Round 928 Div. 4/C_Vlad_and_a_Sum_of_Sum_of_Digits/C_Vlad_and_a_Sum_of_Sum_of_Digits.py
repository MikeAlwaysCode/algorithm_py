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

mx = 2 * 10 ** 5 + 1
p = [0] * (mx)
p[1] = 1
for i in range(2, mx):
    p[i] = p[i - 1] * 2 - p[i - 2] + 1
    x = i
    while x % 10 == 0:
        p[i] -= 9
        x //= 10

def solve() -> None:
    n = sint()
    print(p[n])

for _ in range(int(input())):
    solve()
