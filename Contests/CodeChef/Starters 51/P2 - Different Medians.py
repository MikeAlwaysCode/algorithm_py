from collections import Counter, defaultdict

def solve() -> None:
    n = int(input())
    
    ans = [0] * n

    for i in range(1, n+1):
        if i & 1:
            ans[i-1] = n // 2 + (i + 1) // 2
        else:
            ans[i-1] = i // 2
    
    print(*ans)

t = int(input())
for _ in range(t):
    solve()