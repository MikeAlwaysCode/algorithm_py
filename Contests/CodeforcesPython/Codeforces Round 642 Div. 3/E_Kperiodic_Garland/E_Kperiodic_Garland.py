import math
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
    s = input()

    ans = cnt = s.count('1')

    '''
    pres = [0] * k
    dp = [0] * k
    for i, c in enumerate(s):
        i %= k
        if pres[i]:
            dp[i] = min(dp[i], pres[i]) + (c == '0')
        pres[i] += (c == '1')
        ans = min(ans, dp[i] + cnt - pres[i])

    '''
    dp = [[math.inf] * k for _ in range(3)]
    dp[0] = [0] * k
    for i, c in enumerate(s):
        i %= k
        dp[2][i] = min(dp[1][i], dp[2][i]) + (c == '1')
        dp[1][i] = min(dp[0][i], dp[1][i]) + (c == '0')
        dp[0][i] += c == '1'
        
    
    ans = min(ans, min(min(dp[1][i], dp[2][i]) + cnt - dp[0][i] for i in range(k)))

    print(ans)


for _ in range(int(input())):
    solve()
