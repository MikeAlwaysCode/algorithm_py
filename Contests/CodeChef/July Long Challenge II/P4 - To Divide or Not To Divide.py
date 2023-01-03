# cook your dish here
t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    if a % b == 0:
        print(-1)
    else:
        x = ( n + a - 1 ) // a * a
        while True:
            if x % b != 0:
                break
            x += a
        print(x)
