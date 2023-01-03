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

    fa = list(range(n + 1))
    # cnt = [0] * (n + 1)
    
    def find(x):
        cur = x
        while x != fa[x]:
            x = fa[x]
        if cur != x:
            fa[cur], cur = x, fa[x]
        return x

    ans = 0
    edge = 0
    for bit in range(30):
        x = -1
        for i in range(n):
            if (~ arr[i] >> bit) & 1: continue
            if x != -1 and find(i) != find(x):
                ans += 1 << bit
                edge += 1
                fa[find(i)] = find(x)
            x = i
    print(ans if edge == n - 1 else -1)
    '''
            if (arr[i] >> bit) & 1:
                y = find(i)
                if x == -1:
                    x = y
                elif x == y:
                    continue
                else:
                    ans += 1 << bit
                    fa[y] = x
                    edge += 1
    if edge == n - 1:
        print(ans)
    else:
        print(-1)
    '''

t = int(input())
for _ in range(t):
    solve()