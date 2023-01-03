from itertools import accumulate
import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    A = ints()
    B = ints()
    C = ints()

    pres = []
    pres.append(list(accumulate(A)))
    pres.append(list(accumulate(B)))
    pres.append(list(accumulate(C)))

    tota = sum(A)
    totb = sum(B)
    totc = sum(C)

    if tota == totb == totc:
        mikeEqk = True
    else:
        mikeEqk = False

    # d = {1: "Josh", 0: "Mike", -1:"Nils"}
    josh = mike = nils = -1
    for i in range(n):
        for j in range(3):
            if josh == -1 and pres[j][i] > pres[(j+1)%3][i] and pres[j][i] > pres[(j+2)%3][i]:
                josh = j
            if pres[j][i] < pres[(j+1)%3][i] and pres[j][i] < pres[(j+2)%3][i]:
                if mikeEqk:
                    nils = j
                else:
                    mike = j
    if mikeEqk:
        mike = 3 - josh - nils
    else:
        nils = 3 - josh - mike

    ans = ["", "", ""]
    ans[josh] = "Josh"
    ans[nils] = "Nils"
    ans[mike] = "Mike"

    print(*ans)

t = int(input())
for _ in range(t):
    solve()