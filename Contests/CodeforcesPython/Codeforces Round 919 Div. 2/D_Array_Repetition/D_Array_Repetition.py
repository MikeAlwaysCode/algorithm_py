import sys
from bisect import bisect
from collections import Counter
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
    n, q = mint()
    nums = Counter()
    l = [0]
    for _ in range(n):
        b, x = mint()
        if l[-1] > 10 ** 18:
            continue
        if b == 1:
            l.append(l[-1] + 1)
            nums[len(l) - 1] = x
        else:
            l.append(l[-1] * (x + 1))
    # print(nums)
    # print(l)
    qry = ints()
    ans = []
    for x in qry:
        while True:
            i = bisect(l, x) - 1
            if x == l[i] or x % l[i] == 0:
                if i in nums:
                    ans.append(nums[i])
                    break
                x = l[i - 1]
            else:
                x %= l[i]
                
    print(*ans)


for _ in range(int(input())):
    solve()
