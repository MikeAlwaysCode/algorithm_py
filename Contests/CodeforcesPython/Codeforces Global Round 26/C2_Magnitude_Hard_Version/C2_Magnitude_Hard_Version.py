import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    nums = ints()
    s = mn = 0
    for x in nums:
        s += x
        mn = min(mn, s)
    
    if mn == 0:
        print(pow(2, n, MOD))
        return

    ans = s = positive = 0
    for i, x in enumerate(nums):
        s += x
        if s == mn:
            ans = (ans + pow(2, n - i - 1 + positive, MOD)) % MOD
        if s >= 0:
            positive += 1
    print(ans)

for _ in range(int(input())):
    solve()
