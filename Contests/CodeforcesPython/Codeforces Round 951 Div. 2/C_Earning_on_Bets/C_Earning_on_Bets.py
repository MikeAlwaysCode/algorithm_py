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
    nums = ints()
    x = 10 ** 9
    s = 0
    for k in nums:
        s += x // k + 1
    if s <= x:
        ans = []
        for k in nums:
            ans.append(x // k + 1)
        print(*ans)
    else:
        print(-1)

for _ in range(int(input())):
    solve()
