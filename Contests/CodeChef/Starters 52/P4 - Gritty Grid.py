from collections import Counter, defaultdict

def solve() -> None:
    n, m, x, y = map(int, input().split())
    d = n + m - 2
    
    if (x+y)&1:
        print("Yes")
    elif (d+x)&1:
        print("No")
    else:
        print("Yes")

t = int(input())
for _ in range(t):
    solve()