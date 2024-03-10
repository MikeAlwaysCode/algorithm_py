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
    ans = set()
    for _ in range(n):
        h, m = mint()
        t = h * 60 + m
        ans.add((t - 1) % 1440)
        ans.add((t - 3) % 1440)
        ans.add((t - 5) % 1440)
    
    print(len(ans))
    for t in sorted(ans):
        print(t // 60, t % 60)


solve()
