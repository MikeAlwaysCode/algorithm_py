import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    arr = ints()

    cur = ans = 0
    for i in range(n):
        need = max(0, arr[n - i - 1] - arr[i])
        ans += max(0, need - cur)
        cur = need
        
    '''
    i, j = 0, n - 1
    l = r = ans = 0
    while i < j:
        if arr[i] == arr[j]:
            l = r = 0
        if arr[i] < arr[j]:
            ans += max(0, arr[j] - arr[i] - l)
            l = arr[j] - arr[i]
            r = 0
        else:
            ans += max(0, arr[i] - arr[j] - r)
            l = 0
            r = arr[i] - arr[j]
        i += 1
        j -= 1
    '''
    print(ans)

t = int(input())
for _ in range(t):
    solve()