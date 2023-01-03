from collections import Counter, defaultdict

def solve() -> None:
    n = int(input())
    arra = list(map(int, input().split()))
    arrb = list(map(int, input().split()))

    cnta = cntb = 0
    for a, b in zip(arra, arrb):
        if a > b:
            cnta += a - b
        elif a < b:
            cntb += b - a
    
    if cnta == cntb:
        print(cnta)
    else:
        print(-1)

t = int(input())
for _ in range(t):
    solve()