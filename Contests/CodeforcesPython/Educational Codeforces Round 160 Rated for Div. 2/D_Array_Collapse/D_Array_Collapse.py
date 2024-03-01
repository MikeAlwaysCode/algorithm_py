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
    pres = [0] * (n + 1)
    dp = [0] * n
    stk = []
    s = 0
    for i, x in enumerate(nums):
        while stk and nums[stk[-1]] > x:
            s -= dp[stk.pop()]
        j = 0 if not stk else stk[-1] + 1
        # s 是前面比x小的数的子序列转移到以x结尾的子序列
        # pres[j .. i] 是前面比x大的数的子序列转移到以x结尾的子序列
        # 如果x是nums[0:i]最小的数，即栈为空，本身可以作为一个子序列
        dp[i] = (s + pres[i] - pres[j] + int(not stk)) % MOD
        # 计算子序列前缀和
        pres[i + 1] = (pres[i] + dp[i]) % MOD
        # 栈中所有可以作为结尾的元素的子序列数的和
        s = (s + dp[i]) % MOD
        stk.append(i)
    print(s)


for _ in range(int(input())):
    solve()
