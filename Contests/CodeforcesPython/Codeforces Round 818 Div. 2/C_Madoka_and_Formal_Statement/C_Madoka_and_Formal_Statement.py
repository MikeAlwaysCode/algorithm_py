def solve() -> None:
    n = int(input())
    arra = list(map(int, input().split()))
    arrb = list(map(int, input().split()))

    for i in range(n):
        if arra[i] > arrb[i]:
            print("No")
            return
            
        if arra[i] != arrb[i] and arrb[(i + 1) % n] < arrb[i] - 1:
            print("No")
            return

    print("Yes")

t = int(input())
for _ in range(t):
    solve()