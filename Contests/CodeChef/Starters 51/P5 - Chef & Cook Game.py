from collections import Counter, defaultdict

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    
    x = 0
    for i in range(n):
        if arr[i] & 1:
            x ^= n - i - 1
            
    if x:
        print("Chef")
    else:
        print("Cook")


t = int(input())
for _ in range(t):
    solve()