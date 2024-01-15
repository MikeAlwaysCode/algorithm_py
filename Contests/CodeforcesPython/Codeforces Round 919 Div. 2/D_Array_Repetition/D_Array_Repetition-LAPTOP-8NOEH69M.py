import sys
# from bisect import bisect_left
from collections import Counter
from heapq import *
from random import randint

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
    rd = randint(10 ** 9, 2 * 10 ** 9)
    nums = Counter()
    l = [0]
    for _ in range(n):
        b, x = mint()
        if b == 1:
            nums[len(l)^rd] = x
            l.append(l[-1] + 1)
        else:
            l.append(l[-1] * (x + 1))
    # print(nums)
    # print(l)
    qry = ints()
    h = []
    for i, x in enumerate(qry):
        heappush(h, (-x, i))
    ans = [0] * q
    for i in range(len(l) - 1, 0, -1):
        while h and -h[0][0] >= l[i]:
            x, j = heappop(h)
            x = -x
            if (x == l[i] or x % l[i] == 0) and i ^ rd in nums:
                ans[j] = nums[i ^ rd]
            else:
                if x == l[i] or x % l[i] == 0:
                    x = l[i - 1]
                else:
                    x %= l[i]
                heappush(h, (-x, j))
        if not h:
            break
    print(*ans)


for _ in range(int(input())):
    solve()
