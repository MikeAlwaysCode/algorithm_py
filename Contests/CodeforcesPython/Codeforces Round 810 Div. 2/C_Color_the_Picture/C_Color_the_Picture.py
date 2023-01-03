t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    flag = False
    tot = 0
    for i in range(k):
        if a[i] // n > 2:
            # Could color one more column
            flag = True
        if a[i] // n >= 2:
            tot += a[i] // n
    
    if tot >= m and ( flag or not m & 1):
        print("Yes")
        continue
    
    flag = False
    tot = 0
    for i in range(k):
        if a[i] // m > 2:
            # Could color one more column
            flag = True
        if a[i] // m >= 2:
            tot += a[i] // m
    
    if tot >= n and ( flag or not n & 1):
        print("Yes")
        continue
    
    print("No")