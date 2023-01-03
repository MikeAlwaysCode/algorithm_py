t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    k, m = 0, 0
    v = a[0]
    ans = 0
    for i in range(1, n):
        tmp = a[i] - v
        k = max(k, tmp)
        m = min(m, tmp)
        # if abs(tmp) > 2*x or k - m > 2*x:
        if k - m > 2*x:
            ans += 1
            k, m = 0, 0
            v = a[i]

    print(ans)