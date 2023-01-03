from collections import Counter, defaultdict

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    s = str(input())
    ans = 100
    for i, x in enumerate(s):
        if x == '0':
            ans = min(ans, arr[i])

    print(ans)

t = int(input())
for _ in range(t):
    solve()