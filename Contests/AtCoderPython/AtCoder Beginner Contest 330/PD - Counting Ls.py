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
    col1 = [0] * n
    col2 = [0] * n
    ans = 0
    for _ in range(n):
        s = input()
        cnt = 0
        for i, c in enumerate(s):
            if c == 'o':
                cnt += 1
                ans += col2[i]
        for i, c in enumerate(s):
            if c == 'o':
                col2[i] += cnt - 1
                ans += (cnt - 1) * col1[i]
                col1[i] += 1
    print(ans)

solve()