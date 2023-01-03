# from functools import reduce
from math import lcm, gcd
from collections import Counter, defaultdict
from sortedcontainers import SortedSet, SortedList

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    
    a = arr[0]
    b = 0
    c = arr[-1]
    d = 1000
    ans = 0
    for i in range(n):
        ans = max(ans, arr[i-1] - arr[i])
        if i > 0:
            b = max(b, arr[i])
        if i < n - 1:
            d = min(d, arr[i])
    ans = max(ans, b - a)
    ans = max(ans, c - d)

    print(ans)

t = int(input())
for _ in range(t):
    solve()