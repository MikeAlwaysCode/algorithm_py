import math
t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] * n
    ans = [0] * n
    k = 2

    pos = 0
    for i in range(1, n+1):
        if arr[i-1]:
            continue
        
        arr[i-1] = 1
        ans[pos] = i
        pos += 1
        m = i * 2
        while m <= n and not arr[m-1]:
            arr[m-1] = 1
            ans[pos] = m
            pos += 1
            m *= 2
        
    print(k)
    print(*ans)