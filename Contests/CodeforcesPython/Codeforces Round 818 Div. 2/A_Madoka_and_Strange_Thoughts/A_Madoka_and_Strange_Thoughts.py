def solve() -> None:
    n = int(input())
    ans = n
    ans += n // 3 * 4
    ans += (n // 2 - n // 3) * 2

    print(ans)

t = int(input())
for _ in range(t):
    solve()