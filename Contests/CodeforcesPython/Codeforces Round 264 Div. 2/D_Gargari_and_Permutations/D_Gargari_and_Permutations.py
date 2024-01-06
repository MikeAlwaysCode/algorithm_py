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
    n, k = mint()
    idx = [[0] * (n + 1) for _ in range(k)]
    dp = [1] * (n + 1)
    for i in range(k):
        nums = ints()
        for j, x in enumerate(nums):
            idx[i][x] = j
        
    for i, x in enumerate(nums):
        for j in range(i):
            check = True
            for o in range(k):
                if idx[o][nums[j]] > idx[o][x]:
                    check = False
                    break
            if check:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))


solve()
