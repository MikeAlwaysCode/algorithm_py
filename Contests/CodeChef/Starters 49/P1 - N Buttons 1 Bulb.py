t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    r = str(input())

    ans = 0
    for i in range(n):
        if s[i] != r[i]: ans += 1
    
    print(1 - (ans & 1))