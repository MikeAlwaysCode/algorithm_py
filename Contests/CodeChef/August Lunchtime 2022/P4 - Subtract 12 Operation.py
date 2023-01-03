from collections import Counter, defaultdict

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n-1, 0, -1):
        if arr[i] >= 2:
            k = arr[i] // 2
            arr[i] %= 2
            arr[i-1] -= k

    f = abs(arr[0])
    for i in range(1, n):
        f += abs(arr[i])
        if arr[i] == 1 and arr[i-1] >= 1:
            arr[i] -= 2
            arr[i-1] -= 1
            f -= 1
    print(f)


t = int(input())
for _ in range(t):
    solve()