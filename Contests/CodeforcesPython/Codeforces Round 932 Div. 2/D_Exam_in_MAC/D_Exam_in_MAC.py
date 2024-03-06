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
    n, c = mint()
    nums = ints()
    ans = (c + 2) * (c + 1) // 2
    cnt = [0] * 2
    for x in nums:
        cnt[x & 1] += 1
        m = x // 2
        ans -= m + 1
        ans -= c - x + 1
        ans += cnt[x & 1]
    print(ans)


for _ in range(int(input())):
    solve()
