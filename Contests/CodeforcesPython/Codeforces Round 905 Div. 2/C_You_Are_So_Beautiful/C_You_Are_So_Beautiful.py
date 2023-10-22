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
    suff = [0] * n
    s = set()
    for i in range(n - 1, -1, -1):
        s.add(nums[i])
        suff[i] = len(s)
    ans = 0
    s = set()
    for i, x in enumerate(nums):
        if x not in s:
            ans += suff[i]
            s.add(x)
    print(ans)

for _ in range(int(input())):
    solve()