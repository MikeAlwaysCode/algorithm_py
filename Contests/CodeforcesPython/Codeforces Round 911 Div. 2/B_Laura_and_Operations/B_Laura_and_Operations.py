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
    cnt = ints()
    ans = [0] * 3
    for i in range(3):
        a, b, c = cnt[i], cnt[(i + 1) % 3], cnt[(i + 2) % 3]
        if b == c:
            ans[i] = 1
            continue
        x = abs(b - c)
        if not x & 1 and a:
            ans[i] = 1
    print(*ans)


for _ in range(int(input())):
    solve()
