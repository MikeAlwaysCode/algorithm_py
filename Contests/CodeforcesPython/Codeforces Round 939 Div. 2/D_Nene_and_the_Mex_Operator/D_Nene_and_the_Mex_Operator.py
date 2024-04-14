import sys
# from itertools import accumulate

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
    # pres = list(accumulate(nums, initial=0))
    dp = [[0] * 2 for _ in range(n + 1)]
    for i in range(n):
        dp[i + 1][0] = max(dp[i]) + nums[i]
        for j in range(i + 1):
            dp[i + 1][1] = max(dp[i + 1][1], dp[j][0] + (i - j + 1) ** 2)
    ans = []
    i = n - 1
    while i >= 0:
        if dp[i + 1][0] < dp[i + 1][1]:
            for j in range(i + 1):
                if dp[i + 1][1] == dp[j][0] + (i - j + 1) ** 2:
                    fop = []
                    for k in range(j, i + 1):
                        if nums[k] != k - j:
                            ans.append((j + 1, k + 1))
                            ans.extend(fop)
                        fop.append((j + 1, k + 1))
                        fop.extend(fop[:-1])
                    ans.append((j + 1, i + 1))
                    i = j - 1
                    break
        else:
            i -= 1
    print(max(dp[-1]), len(ans))
    for l, r in ans:
        print(l, r)


solve()
