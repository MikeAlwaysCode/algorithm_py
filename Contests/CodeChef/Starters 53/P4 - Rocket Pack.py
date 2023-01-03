from collections import Counter, defaultdict

def solve() -> None:
    n, m, k = map(int, input().split())
    battery = []
    for _ in range(k):
        x, y, c, e = map(int, input().split())
        battery.append((x+y, c, e))
        
    battery.append(n+m, 0, 0)
    battery.sort()
    
    cost = [0] * (n+m+1)
    energy = [0] * (n+m+1)
    visit = [False] * (n+m+1)
    visit[0] = True
    # for bat in battery:
        

t = int(input())
for _ in range(t):
    solve()