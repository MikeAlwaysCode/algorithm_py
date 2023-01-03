def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    s, e = 0, n - 1
    while s < e:
        l = r = False
        if arr[s+1] >= arr[s]:
            s += 1
        else:
            l = True
        if arr[e-1] >= arr[e]:
            e -= 1
        else:
            r = True
        
        if l and r: break
    
    if s >= e:
        print("Yes")
    else:
        print("No")

t = int(input())
for _ in range(t):
    solve()