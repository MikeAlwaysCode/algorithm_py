t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # arr = list(map(int, input().split()))
    # ans = n * m - ( n - n & 1 ) * ( m - m & 1 )
    ans = ( n & 1 ) * m + ( m & 1 ) * n - ( n & 1 ) * ( m & 1 )
    
    print(ans)