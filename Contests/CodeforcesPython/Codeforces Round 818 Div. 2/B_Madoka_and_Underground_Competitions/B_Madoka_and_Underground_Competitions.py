def solve() -> None:
    n, k, r, c = map(int, input().split())
    res = [['.'] * n for _ in range(n)]

    rk = (r-1) % k
    ck = (c-1) % k
    mx = max(rk, ck)
    for i in range(n):
        j = i % k
        if i % k == rk:
            j = ck
        elif i % k == ck:
            j = rk
        while j < n:
            res[i][j] = 'X'
            j += k
    
    for i in range(n):
        print("".join(res[i]))

t = int(input())
for _ in range(t):
    solve()