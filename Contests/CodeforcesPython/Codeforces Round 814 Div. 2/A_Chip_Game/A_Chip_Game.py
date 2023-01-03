def solve() -> None:
    n, m = map(int, input().split())
    
    a = 0 if n == 1 else 2 if n&1 else 1
    b = 0 if m == 1 else 2 if m&1 else 1

    if (a^b)&1:
        print("Burenka")
    else:
        print("Tonya")

t = int(input())
for _ in range(t):
    solve()