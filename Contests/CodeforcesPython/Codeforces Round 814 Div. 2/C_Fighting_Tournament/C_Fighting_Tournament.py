def solve() -> None:
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    preWin = [0] * n
    posWin = [0] * n
    maxStrength = arr[0]
    idx = 0
    for i in range(1, n):
        if arr[i] >maxStrength:
            preWin[i] = 1
            idx = i
            maxStrength = arr[i]
        else:
            posWin[idx] += 1
        # maxStrength = max(maxStrength, arr[i])
    posWin[idx] = 10 ** 10
        # print(preWin)
        # print(posWin)
    for _ in range(q):
        i, r = map(int, input().split())
        ans = preWin[i-1] if r >= i-1 else 0
        ans += min(posWin[i-1], max(0, r - i + 1))
        print(ans)
        
t = int(input())
for _ in range(t):
    solve()