def solve() -> None:
    n = int(input())

    if n == 1:
        ans = 2
    elif n == 2:
        ans = 1
    else:
        ans = n // 3
        if n % 3 > 0:
            ans += 1
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()