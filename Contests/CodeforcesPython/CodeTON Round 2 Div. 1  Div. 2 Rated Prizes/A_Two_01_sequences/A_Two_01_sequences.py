t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = str(input())
    b = str(input())

    if n == m:
        if a == b:
            print("YES")
        else:
            print("No")
    else:
        k = n - m
        if a[k:] == b:
            print("YES")
        elif a[k+1:] != b[1:]:
            print("NO")
        else:
            chk = False
            for x in a[:k]:
                if x == b[0]:
                    chk = True
                    break
            if chk:
                print("YES")
            else:
                print("NO")
