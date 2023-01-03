from collections import Counter, defaultdict, deque
# from sortedcontainers import SortedSet, SortedList

def solve() -> None:
    n, q = map(int, input().split())

    ans = [0] * n
    cnt = [0] * (n + 1)

    k = 1
    for _ in range(q):
        l, r = map(int, input().split())
        cnt[l] += 1
        cnt[r] -= 1
        k = max(k, r - l + 1)

    listen = 0
    ans[0] = 1

    for i in range(n):
        listen += cnt[i]
        if listen == 0:
            if i > 0:
                ans[i] = ans[i-1]
        else:
            ans[i] = ans[i-1] + 1
            if ans[i] > k:
                ans[i] %= k

    print(k)
    print(*ans)

# t = int(input())
# for _ in range(t):
solve()