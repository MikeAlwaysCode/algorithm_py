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
    s = input()
    n, ans = len(s), 0
    
    dp = [0] * (n + 1)
    for i in range(n):
        for j in range(n - 1, i, -1):
            dp[j + 1] = dp[j] + 1 if s[i] == s[j] or s[i] == '?' or s[j] == '?' else 0
            if dp[j + 1] >= j - i:
                ans = max(ans, (j - i) * 2)

    '''
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = int(s[i] == s[j] or s[i] == '?' or s[j] == '?')
            if dp[i][j] and i:
                dp[i][j] += dp[i - 1][j - 1]
            if dp[i][j] >= j - i:
                ans = max(ans, (j - i) * 2)
    '''
    print(ans)

for _ in range(int(input())):
    solve()
