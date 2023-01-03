t = int(input())

for _ in range(t):
    n = int(input())
    res = 0
    p = 1
    d = 9
    while n > 0:
        if d > n:
            d = n
        
        res += d * p
        n -= d
        p *= 10
        d -= 1

    print(res)