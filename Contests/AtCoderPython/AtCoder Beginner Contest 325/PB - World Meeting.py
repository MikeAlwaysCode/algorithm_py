import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    base = []
    for _ in range(n):
        base.append(tuple(mint()))
    
    ans = 0
    for t in range(24):
        cnt = 0
        for w, x in base:
            xt = (t + x) % 24
            if 9 <= xt < 18:
                cnt += w
        ans = max(ans, cnt)

    print(ans)

solve()