def solve() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d1 = [0] * n
    d2 = [0] * n

    l = r = n - 1
    last = n
    for i in range(n-1, -1, -1):
        while l > 0 and b[l-1] >= a[i]:
            l -= 1
        
        d1[i] = b[l] - a[i]
        d2[i] = b[r] - a[i]

        if r - l + 1 == last - i:
            last = i
            l = r = l - 1

    print(*d1)
    print(*d2)

t = int(input())
for _ in range(t):
    solve()