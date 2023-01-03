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
    
    ans = 0
    l, r = 0, n - 1
    while l < r:
        if arr[l] == arr[r]:
            l += 1
            r -= 1
        elif arr[l] > arr[r]:
            arr[l] -= arr[r]
            r -= 1
            ans += 1
        else:
            arr[r] -= arr[l]
            l += 1
            ans += 1
    '''
    q = collections.deque(arr)
    while len(q) > 1:
        if q[0] == q[-1]:
            q.popleft()
            q.pop()
            continue
        elif q[0] > q[-1]:
            x = q.popleft()
            q.appendleft(x - q[-1])
            q.pop()
        else:
            x = q.pop()
            q.append(x - q[0])
            q.popleft()
        ans += 1
    '''
    print(ans)

t = int(input())
for _ in range(t):
    solve()