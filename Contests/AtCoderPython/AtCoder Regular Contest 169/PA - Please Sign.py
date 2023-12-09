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
    nums = ints()
    p = ints()
    g = [[] for _ in range(n)]
    for i, u in enumerate(p, 1):
        g[u - 1].append(i)

    ans, s, last = nums[0], 0, 0
    q = g[0]
    while q:
        tmp = q
        q = []
        last = 0
        for u in tmp:
            last += nums[u]
            q.extend(g[u])
        s += last
        ans += s
    if last == 0:
        if s == 0:
            print(0 if ans == 0 else "+" if ans > 0 else "-")
        else:
            print("+" if s > 0 else "-")
    else:
        print("+" if last > 0 else "-")


solve()
