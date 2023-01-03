t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    v = [0] * (n+1)
    ans = 0
    for i in range(n-1, -1, -1):
        v[a[i]] += 1
        if v[a[i]] > 1:
            ans = i + 1
            break
    
    print(ans)