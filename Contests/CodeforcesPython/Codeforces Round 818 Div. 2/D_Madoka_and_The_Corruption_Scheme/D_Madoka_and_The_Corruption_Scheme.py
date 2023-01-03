def solve() -> None:
    MOD = 10 ** 9 + 7

    n, k = map(int, input().split())

    ans = pow(2, n-1, MOD) + 2 * k - 1
    ans %= MOD

    print(ans)


# t = int(input())
# for _ in range(t):
solve()