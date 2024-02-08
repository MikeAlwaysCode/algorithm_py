import sys
from collections import deque
# from heapq import *

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
    n, m = mint()
    nums = ints()
    ans = []
    s = 0
    seen = set(nums)
    # h = []
    h = deque()
    for x in nums:
        if x - 1 not in seen:
            h.append((1, x - 1, -1))
            seen.add(x - 1)
        if x + 1 not in seen:
            h.append((1, x + 1, 1))
            seen.add(x + 1)
    # heapify(h)
    for _ in range(m):
        # d, x, step = heappop(h)
        d, x, step = h.popleft()
        s += d
        ans.append(x)
        if x + step not in seen:
            # heappush(h, (d + 1, x + step, step))
            h.append((d + 1, x + step, step))
            seen.add(x + step)
    print(s)
    print(*ans)


solve()
