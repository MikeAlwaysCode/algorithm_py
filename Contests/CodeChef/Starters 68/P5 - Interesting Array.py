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

    if n <= 2:
        print(*arr)
        return

    arr.sort()
    if arr[0] == arr[-1]:
        print(-1)
        return
    
    ans = []
    m = (n - 1) // 2
    i, j = m, n - 1
    while j > m:
        if arr[i] == arr[j]:
            print(-1)
            return
        ans.append(arr[i])
        ans.append(arr[j])
        i -= 1
        j -= 1
    if i == 0:
        ans.append(arr[i])
    
    if ans[-1] == ans[-2]:
        print(-1)
        print(*ans)
    else:
        print(*ans)

t = int(input())
for _ in range(t):
    solve()