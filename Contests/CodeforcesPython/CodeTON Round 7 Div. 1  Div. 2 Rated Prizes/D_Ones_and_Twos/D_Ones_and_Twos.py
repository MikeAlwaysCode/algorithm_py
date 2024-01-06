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
    n, q = mint()
    nums = ints()
    mn, mx = [], []
    s = 0
    for i, x in enumerate(nums):
        if x == 1:
            heappush(mn, i)
            heappush(mx, -i)
        s += x

    for _ in range(q):
        qry = ints()
        if qry[0] == 1:
            v = qry[1]
            if v > s:
                print("NO")
                continue
            if v & 1 == s & 1:
                # If s exist, then "s - 2" will exist
                print("YES")
                continue
            if not mn:
                print("NO")
                continue
            l, r = mn[0], -mx[0]
            # after the first 1 or before the last 1, the parity will change
            if v <= s - l * 2 - 1 or v <= s - (n - r) * 2 + 1:
                print("YES")
            else:
                print("NO")
        else:
            i, v = qry[1] - 1, qry[2]
            s += v - nums[i]
            nums[i] = v
            if v == 1:
                heappush(mn, i)
                heappush(mx, -i)
            while mn and nums[mn[0]] != 1:
                heappop(mn)
            while mx and nums[-mx[0]] != 1:
                heappop(mx)


for _ in range(int(input())):
    solve()
