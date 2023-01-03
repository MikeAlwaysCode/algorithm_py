from collections import Counter, defaultdict

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    # a = b = 0

    # for x in arr:
    #     a += x
    #     b = max(b, a) + x

    # print(b)

    ans = sum(arr) + max(arr)
    print(ans)

t = int(input())
for _ in range(t):
    solve()