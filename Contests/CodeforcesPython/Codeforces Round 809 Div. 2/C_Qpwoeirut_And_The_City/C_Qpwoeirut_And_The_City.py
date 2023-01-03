t = int(input())

def addFloor(i: int) -> int:
    return max(h[i-1]+1-h[i], h[i+1]+1-h[i], 0)

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    '''
    m = n % 2
    
    if m:
        ans = 0
        for i in range(1, n-1, 2):
            cs = addFloor(i)
            ans += cs
        
        print(ans)
        continue

    dp = [10**15] * n
    dp[0], dp[1] = 0, 0
    dp[2] = addFloor(1)

    if n == 3:
        print(dp[2])
        continue

    dp[3] = min(addFloor(1), addFloor(2))
    
    if n == 4:
        print(dp[3])
        continue

    # dp[4] = dp[2] + addFloor(3)

    for i in range(5, n, 2):
        dp[i] = min(dp[i-2] + addFloor(i-1), dp[i-3] + min(addFloor(i-1), addFloor(i-2)))

    # if n == 12:
    #     print(dp)

    print(dp[n-1])
    '''
    ans = 10**9 * 10**5
    dp = [0] * n
    for i in range(2, n):
        dp[i] = dp[i-2] + addFloor(i-1)

    if n & 1:
        ans = dp[n-1]
    else:
        for i in range(0, n, 2):
            ans = min(ans, dp[n-1] + dp[i] - dp[i+1])
    
    print(ans)