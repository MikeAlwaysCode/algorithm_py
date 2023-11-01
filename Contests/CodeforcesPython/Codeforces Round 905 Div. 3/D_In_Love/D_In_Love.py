import sys
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
    n = 0
    lh = []
    rh = []
    cntl, cntr = Counter(), Counter()
    h = randint(1, 1 << 30)
    for _ in range(sint()):
        qry = input().split()
        l, r = int(qry[1]), int(qry[2])
        if qry[0] == '+':
            n += 1
            cntl[l ^ h] += 1
            cntr[r ^ h] += 1
            if cntl[l ^ h] == 1:
                heappush(lh, -l)
            if cntr[r ^ h] == 1:
                heappush(rh, r)
        else:
            n -= 1
            cntl[l ^ h] -= 1
            cntr[r ^ h] -= 1
            while lh and cntl[(-lh[0]) ^ h] == 0:
                heappop(lh)
            while rh and cntr[rh[0] ^ h] == 0:
                heappop(rh)
        print("YES" if n > 1 and lh[0] + rh[0] < 0 else "NO")

solve()