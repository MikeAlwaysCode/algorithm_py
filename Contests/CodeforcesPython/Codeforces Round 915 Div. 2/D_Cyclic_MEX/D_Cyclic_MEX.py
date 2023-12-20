import sys
from collections import deque

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
    n = sint()
    p = ints()
    p.extend(p)
    ans = s = j = 0
    q = deque()
    for i, x in enumerate(p):
        if i - j >= n:
            if q and q[0] <= j:
                q.popleft()
            if q:
                s -= p[q[0]]
            j += 1
        while q and p[q[-1]] > x:
            k = q.pop()
            if q:
                s -= p[k] * (k - q[-1])
            else:
                s -= p[k] * (k - j)
        if q:
            s += x * (i - q[-1])
        else:
            s += x * (i - j)
        q.append(i)
        if i >= n - 1:
            ans = max(ans, s)

    print(ans + n)


for _ in range(int(input())):
    solve()
