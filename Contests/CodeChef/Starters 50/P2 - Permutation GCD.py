from collections import Counter, defaultdict

def solve() -> None:
    n, x = map(int, input().split())
    '''
    if x < n:
        print(-1)
        return
    
    ans = list()
    ans.append(x - n + 1)
    for i in range(1, n+1):
        if i == ans[0]:
            continue
        ans.append(i)
    
    print(*ans)
    '''
    if x < n:
        print(-1)
    else:
        k = x - n + 1
        print(k, *range(1, k), *range(k+1, n+1))
t = int(input())
for _ in range(t):
    solve()