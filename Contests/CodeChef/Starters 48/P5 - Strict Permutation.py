t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = []
    for i in range(m):
        x, y = map(int, input().split())
        arr.append((x, y))

    ans = []
    
    print(arr)