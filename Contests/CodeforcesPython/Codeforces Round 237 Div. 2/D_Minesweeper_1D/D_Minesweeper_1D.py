import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    s = input()
    dp = [0] * 3
    dp[0] = dp[2] = 1
    for x in s:
        if x == '0':
            dp[1] = dp[2] = 0
        elif x == '1':
            dp[0], dp[1], dp[2] = dp[1], 0, dp[0]
        elif x == '2':
            dp[0], dp[1], dp[2] = 0, 0, dp[1]
        elif x == '*':
            dp[0], dp[1] = 0, dp[2]
        else:
            dp[0], dp[1], dp[2] = (dp[0] + dp[1]) % MOD, dp[2], sum(dp) % MOD
            
    print((dp[0] + dp[1]) % MOD)

solve()