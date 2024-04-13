import sys
from heapq import *

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
    n, p, s = mint()
    A = ints()
    B = ints()

    seen = [0] * n
    idx = sorted(range(n), key = lambda x: -A[x])
    ans = 0
    h1, h2, h3 = [], [], []
    for i in idx[:p]:
        seen[i] = 1
        ans += A[i]
        heappush(h3, (A[i] - B[i], i))
    for i in range(n):
        if seen[i] == 0:
            heappush(h1, (-A[i], i))
            heappush(h2, (-B[i], i))
    for _ in range(s):
        while h1 and seen[h1[0][1]] != 0:
            heappop(h1)
        while h2 and seen[h2[0][1]] != 0:
            heappop(h2)
        if -h2[0][0] >= -h1[0][0] - h3[0][0]:
            ans -= h2[0][0]
            seen[heappop(h2)[1]] = 2
        else:
            ans -= h3[0][0]
            seen[heappop(h3)[1]] = 2
            x, i = heappop(h1)
            ans -= x
            heappush(h3, (A[i] - B[i], i))
            seen[i] = 1
    arr1 = [i + 1 for i, v in enumerate(seen) if v == 1]
    arr2 = [i + 1 for i, v in enumerate(seen) if v == 2]
    print(ans)
    print(*arr1)
    print(*arr2)


solve()
