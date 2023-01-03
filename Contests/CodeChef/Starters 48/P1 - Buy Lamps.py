t = int(input())
for _ in range(t):
    n, k, x, y = map(int, input().split())
    # arr = list(map(int, input().split()))

    ans = k * x + (n - k) * min(x, y)
    
    print(ans)