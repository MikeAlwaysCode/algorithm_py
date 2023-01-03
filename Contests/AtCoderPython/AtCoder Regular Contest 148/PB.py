import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    s = input().strip()
    l = s.find("p")
    if l == -1:
        print(s)
        return
    pres = "d"
    pr = l
    ans = s[:l] + pres + s[l + 1:]
    for r in range(l + 1, n):
        if s[r] == "p":
            npres = ""
            for j in range(r, pr, -1):
                if s[j] == "p":
                    npres += "d"
                else:
                    npres += "p"
            pres = npres + pres
            pr = r

            curs = s[:l] + pres + s[r + 1:]
            if curs < ans:
                ans = curs

    print(ans)

# t = int(input())
# for _ in range(t):
solve()