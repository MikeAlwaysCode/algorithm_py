from collections import Counter, defaultdict

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = Counter(arr)

    if cnt.most_common(1)[0][1] > (n + 1) // 2:
        print("No")
    else:
        print("Yes")

t = int(input())
for _ in range(t):
    solve()