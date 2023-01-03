t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    ans = ['B'] * m

    for d in a:
        s = min(d, m + 1 - d)
        l = max(d, m + 1 - d)

        if ans[s-1] == 'B':
            ans[s-1] = 'A'
        elif ans[l-1] == 'B':
            ans[l-1] = 'A'
    
    print("".join(ans))