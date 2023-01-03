t = int(input())

for _ in range(t):
    n = int(input())
    ans = [i for i in range(n)]
    ans[0] = n
    
    print(*ans)