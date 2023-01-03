t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    ans, count = 0, 0
    for a in arr:
        if a == 1:
            count += 1
        elif count > 0:
            ans += ( count + 1 ) * count // 2
            count = 0

    if count > 0: ans += ( count + 1 ) * count // 2
    
    print(ans)
