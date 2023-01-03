from collections import Counter, defaultdict
# from sortedcontainers import SortedSet, SortedList

def solve() -> None:
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt1 = [0] * (n + 1)
    cnt2 = [0] * (n + 1)

    for i, a in enumerate(arr):
        cnt1[i+1] = cnt1[i] + a
        cnt2[i+1] = cnt2[i] + a * (i + 1)

    ans = - 10 ** 20
    for i in range(m, n+1):
        s1 = cnt1[i] - cnt1[i-m]
        s2 = cnt2[i] - cnt2[i-m]

        ans = max(ans, s2 - s1 * (i-m))

    print(ans)

solve()