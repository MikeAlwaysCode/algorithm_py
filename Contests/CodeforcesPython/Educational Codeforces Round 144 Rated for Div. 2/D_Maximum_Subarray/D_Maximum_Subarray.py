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
    n, k, x = map(int, input().split())
    arr = ints()
    
    ans = 0
    dp = [0] * (k + 1)
    for i in range(n):
        for j in range(min(i + 1, k), -1, -1):
            if j <= i:
                dp[j] = max(0, dp[j] + arr[i] - x)
            elif j > i:
                dp[j] = max(0, dp[j - 1] + arr[i] + x)
            if j:
                dp[j] = max(dp[j], dp[j - 1] + arr[i] + x)
            
            if k - j < n - i: ans = max(ans, dp[j])
        
    print(ans)


for _ in range(int(input())):
    solve()
