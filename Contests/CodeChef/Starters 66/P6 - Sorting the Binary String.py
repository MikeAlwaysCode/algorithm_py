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
    s = input()

    ans = 0
    
    '''
    p1 = p2 = p3 = p4 = n
    for i in reversed(range(n)):
        if s[i] == '1':
            zeros = []
            for j in range(p1, p2):
                if s[j] == '0': zeros.append(j)
            if len(zeros) > 1:
                p3 = zeros[0]
                p4 = zeros[1]
            elif len(zeros) == 1:
                p4 = p3
                p3 = zeros[0]
            p2 = p1
            p1 = i
        ans += p4 - i
    '''
    r = n - 1
    pos0 = collections.deque()
    cnt0 = cnt1 = inv = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '0':
            cnt0 += 1
            pos0.append(i)
        else:
            cnt1 += 1
            inv += cnt0
        
        while pos0 and inv >= pos0[0] - i + 1:
            if s[r] == '0':
                cnt0 -= 1
                inv -= cnt1
                pos0.popleft()
            else:
                cnt1 -= 1
            r -= 1
        
        ans += r - i + 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()