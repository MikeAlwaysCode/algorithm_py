def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    c = arr.copy()
    c.sort()
    
    mn1 = c[0]
    mn2 = c[1]
    mx1 = c[-1]
    mx2 = c[-2]
    
    print(mx1 + mx2 - mn1 - mn2)

t = int(input())
for _ in range(t):
    solve()