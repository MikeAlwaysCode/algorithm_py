from collections import Counter, defaultdict

def solve() -> None:
    n, m = map(int, input().split())
    arra = [[] for _ in range(n)]
    arrb = [[] for _ in range(n)]
    for i in range(n):
        arra[i] = list(map(int, input().split()))
    for i in range(n):
        arrb[i] = list(map(int, input().split()))
    
    if n == 1 or m == 1:
        print("Yes" if arra == arrb else "No")
        return

    aCounterEven = defaultdict(int)
    aCounterOdd = defaultdict(int)
    bCounterEven = defaultdict(int)
    bCounterOdd = defaultdict(int)

    for i in range(n):
        for j in range(m):
            if arra[i][j] == arrb[i][j]:
                continue

            if (i + j)&1:
                aCounterOdd[arra[i][j]] += 1
                bCounterOdd[arrb[i][j]] += 1
            else:
                aCounterEven[arra[i][j]] += 1
                bCounterEven[arrb[i][j]] += 1

    if aCounterEven == bCounterEven and aCounterOdd == bCounterOdd:
        print("Yes")
    else:
        print("No")

t = int(input())
for _ in range(t):
    solve()