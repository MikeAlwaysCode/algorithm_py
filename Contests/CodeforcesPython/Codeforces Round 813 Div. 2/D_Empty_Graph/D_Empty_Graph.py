def solve() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    x = 10 ** 9

    if k == n:
        print(x)
        return

    a.sort()

    if k >= 2:
        print(min(a[k] * 2, x))
        return

    ans = a[k]

    for i in range(k+1, n):
        if a[i] >= a[k] * 2:
            ans = a[k] * 2
            break
        ans = max(ans, a[i])

    print(ans)

t = int(input())
for _ in range(t):
    solve()