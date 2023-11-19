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

palindrome = []
dp = [0] * (4 * 10 ** 4 + 1)

def init():
    for i in range(1, 400):
        x = str(i)
        palindrome.append(int(x + x[-2::-1]))
        if i < 100:
            palindrome.append(int(x + x[::-1]))
    dp[0] = 1
    for v in palindrome:
        for i in range(v, len(dp)):
            dp[i] = (dp[i] + dp[i - v]) % MOD

def solve() -> None:
    n = sint()
    print(dp[n])

init()
for _ in range(int(input())):
    solve()