import collections
import math
import random
import sys
from functools import *
from heapq import *
from string import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n, k = map(int, input().split())
    
    s = str(n)
    if len(set(s)) <= k:
        print(0)
        return

    m = len(s)
    mark = [0] * 10
    ans = ""
    def check(t):
        st = set(t)
        if len(st) > k:
            return False
        if len(st) == k:
            ma = max(st)
            while len(t) < len(s):
                t += ma
        else:
            while len(t) < len(s):
                t += '9'
        return int(t) >= n
    for i in range(len(s)):
        f = int(s[i])
        for j in digits[f:]:
            if check(ans + str(j)):
                ans += str(j)
                break
    print(int(ans) - n)

    '''
    dp = [[math.inf] * (1<<10) for _ in range(m + 1)]
    dp[m][0] = 0
    p = 1
    for i in range(m - 1, -1, -1):
        for mask in range(1<<10):
            if dp[i+1][mask] == math.inf:
                continue
            carry = dp[i+1][mask]
            if i < m - 1:
                carry += s[i + 1] * p // 10
            cur = s[i] +  carry // p
            cnt = bin(mask).count('1')
            for d in range(10):
                if not mask >> d & 1 and cnt == k:
                    continue
                add = d - cur if d >= cur else d + 10 - cur
                add *= p
                dp[i][mask|(1<<d)] = min(dp[i][mask|(1<<d)], dp[i+1][mask] + add)
        p *= 10
    print(min(dp[0]))
    '''
    '''
    @lru_cache()
    def f(i: int, mask: int, cnt: int, carry: int):
        if cnt > k:
            return math.inf
        if i < 0:
            return 0
        cur = s[i] + carry
        res = math.inf
        low = 0 if i > 0 else cur
        for d in range(low, 10):
            add = d - cur if d >= cur else d + 10 - cur
            add *= pow(10, m - i - 1)
            nr = add + f(i - 1, mask|(1<<d), cnt + (not mask >> d & 1), d < cur)
            if nr < res:
                res = nr
        return res
        
    print(f(m - 1, 0, 0, 0))
    '''

for _ in range(int(input())):
# for _ in range(1):
    solve()