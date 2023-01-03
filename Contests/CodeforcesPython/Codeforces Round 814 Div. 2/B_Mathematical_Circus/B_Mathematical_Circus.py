def solve() -> None:
    n, k = map(int, input().split())

    if k == 0:
        print("NO")
    elif k&1:
        print("YES")
        for i in range(1, n, 2):
            print(i, i +1)
    else:
        if k%4 == 0:
            print("NO")
        else:
            print("YES")
            m = 4 - k%4
            i = (m+1)%4
            j = 1
            while i <= n:
                print(i, j*4)
                i += 4
                j += 1
            i = (m-1)%4
            j = m
            while i <= n:
                print(j, i)
                i += 4
                j += 4

t = int(input())
for _ in range(t):
    solve()