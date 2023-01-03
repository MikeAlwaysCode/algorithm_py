# cook your dish here
t = int(input())
for _ in range(t):
    x, y, n, r = map(int, input().split())
    if x == y:
        if r >= y * n:
            print(0, n)
        else:
            print(-1)
    else:
        b = min(( r - x * n ) // ( y - x ), n)
        if b < 0:
            print(-1)
        else:
            print(n-b, b)
