import sys
from collections import deque
from heapq import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, m, k = mint()
    color = ints()
    pos = [deque() for _ in range(n + 1)]
    cnt = [0] * (n + 1)
    last = [-1] * (n + 1)
    h = []
    s = 0
    for i, c in enumerate(color):
        cnt[c] += 1
        pos[c].append(i)
        if len(pos[c]) == 1:
            heappush(h, (i, 0, c))
        
    for _ in range(m):
        i, j, c = heappop(h)
        if j + k >= len(pos[c]):
            s += len(pos[c] - j + 1)
        else:
            s += k
            j += k
            heappush(h, (pos[c][j], j, c))
        if not h:
            break

    print(s)
    for i in range(0, n - 1):
        c = color[i]
        pos[c].popleft()
        pos[c].append(n + i)
        s -= min(cnt[c], k)
        heappush(h, (pos[c][0], c))
        i, c = heappop(h)
        s += cnt[c]
        print(s)

solve()
