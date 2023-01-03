import copy


def solve() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = set(a[:k])
    # print(s)
    a.sort()
    ans = 0
    for i in range(k):
        if a[i] not in s:
            ans += 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()