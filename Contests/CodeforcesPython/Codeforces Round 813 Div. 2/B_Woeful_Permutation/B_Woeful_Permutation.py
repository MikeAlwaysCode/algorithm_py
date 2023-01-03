def solve() -> None:
    n = int(input())

    ans = [1] * n

    i = 1 if n&1 else 0

    while i < n-1:
        ans[i] = i + 2
        ans[i+1] = i + 1
        i += 2

    print(*ans)
    

t = int(input())
for _ in range(t):
    solve()