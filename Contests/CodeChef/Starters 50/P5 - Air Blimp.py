from collections import Counter, defaultdict

def solve() -> None:
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))

    # arr.sort()

    if x <= y:
        ans = (max(arr) + y - 1) // y
        print(ans)
        return
        
    ans = 0
    for i in range(n-1, -1, -1):
        if arr[i] > ans * y:
            ans += (arr[i] - ans * y + x - 1) // x
    
    print(ans)
    
    '''
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = (arr[0] + y - 1) // y
    dp[0][1] = (arr[0] + x - 1) // x

    for i in range(1, n):
        ty = (arr[i] + y - 1) // y
        tx = (arr[i] + x - 1) // x
        # print("ty", ty)
        # print("tx", tx)
        dp[0][i] = min(max(ty, dp[0][i-1]), (max(dp[1][i-1] * x - ty * y, 0) + x - 1) // x + ty)
        dp[1][i] = min(max(tx, dp[0][i-1]), (max(dp[1][i-1] * x - tx * y, 0) + x - 1) // x + tx)
    
    print(min(dp[0][n-1], dp[1][n-1]))
    '''
t = int(input())
for _ in range(t):
    solve()