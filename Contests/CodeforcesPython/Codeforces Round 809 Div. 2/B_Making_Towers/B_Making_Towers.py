t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0] * n

    p = [0] * n

    for i, c in enumerate(a):
        # print(c,",",i)
        if ans[c-1] == 0:
            ans[c-1] += 1
            p[c-1] = i
        elif (i - p[c-1]) % 2 == 1:
            ans[c-1] += 1
            p[c-1] = i
    
    print(*ans)