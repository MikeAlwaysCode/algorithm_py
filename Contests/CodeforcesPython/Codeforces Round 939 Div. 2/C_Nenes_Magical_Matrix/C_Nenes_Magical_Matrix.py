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
    ans = 0
    op = []
    p = list(range(n, 0, -1))
    for i in range(1, n + 1):
        op.append([2, i] + p)
        op.append([1, i] + p)
        ans += i * (i * 2 - 1)
    print(ans, len(op))
    for o in op:
        print(*o)


for _ in range(int(input())):
    solve()
