def countone(oneNum) -> int:
    return ( oneNum + 1 ) * oneNum // 2

MODULE = 998244353
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    count1, count0 = 0, 0
    for a in arr:
        if a == 1:
            count1 += 1
        else:
            count0 += 1

    ans = 0
    for i in range(count0 + 1):

    
    for a in arr:
        if a == 1:
            count += 1
        elif count > 0:
            ans += countone(count)
            count = 0

    if count > 0: ans += countone(count)
    
    print(ans)
