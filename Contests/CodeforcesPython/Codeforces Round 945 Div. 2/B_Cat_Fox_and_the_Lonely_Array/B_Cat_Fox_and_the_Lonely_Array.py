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
    ans = 1
    for bit in range(20):
        p = -1
        for i, x in enumerate(nums):
            if x >> bit & 1:
                ans = max(ans, i - p)
                p = i
        if p != -1:
            ans = max(ans, n - p)
    print(ans)


for _ in range(int(input())):
    solve()
