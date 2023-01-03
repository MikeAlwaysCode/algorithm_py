from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    if arr[0] == arr[-1]:
        print(0)
        continue

    tot = sum(arr)
    cur, ans = 0, n

    for i, a in enumerate(arr):
        cur += a
        x = tot - cur
        if x >= a * (i + 1) - cur:
            ans = min(ans, n - i - 1)
    
    print(ans)