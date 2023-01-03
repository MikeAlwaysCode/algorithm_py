def solve() -> None:
    n = int(input())
    ans = [i+1 for i in range(n)]

    print(n)
    print(*ans)
    for i in range(1, n):
        tmp = ans[i-1]
        ans[i-1] = ans[i]
        ans[i] = tmp
        print(*ans)

t = int(input())
for _ in range(t):
    solve()