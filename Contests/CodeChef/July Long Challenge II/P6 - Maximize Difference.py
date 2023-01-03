# cook your dish here
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    c = m // n
    a = m // c
    b = a * c
    
    maxdif = abs(a - b)
    na = n
    h = min(a * 2, m)
    while na < h:
        nb = m // na * na
        if abs(na - nb) > maxdif:
            maxdif = abs(na - nb)
            a, b = na, nb
        
        na += 1

    print(a, b)
