import sys
from bisect import bisect

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, m, k = mint()
    A = ints()
    D = ints()
    F = ints()
    cnt = mx = l = r = sec = 0
    for i in range(1, n):
        if A[i] - A[i - 1] > mx:
            sec = mx
            mx, cnt, l, r = A[i] - A[i - 1], 1, A[i - 1], A[i]
        elif A[i] - A[i - 1] == mx:
            cnt += 1
        elif A[i] - A[i - 1] > sec:
            sec = A[i] - A[i - 1]
    if cnt > 1:
        print(mx)
        return
    
    ans = mx
    mid = (l + r) // 2
    D.sort()
    F.sort()
    for x in D:
        if x >= r:
            break
        j = bisect(F, mid - x)
        if j and l <= F[j - 1] + x <= r:
            ans = min(ans, max(F[j - 1] + x - l, r - F[j - 1] - x, sec))
        if j < k and l <= F[j] + x <= r:
            ans = min(ans, max(F[j] + x - l, r - F[j] - x, sec))
    print(ans)


for _ in range(int(input())):
    solve()
