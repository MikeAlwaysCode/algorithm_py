import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    s = input()
    
    def printAns(s: str, k: int):
        ans = 0
        n = len(s)
        pow2 = 1
        for i in range(n-1, k-1, -1):
            if s[i] == '1':
                ans = (ans + pow2) % MOD
            pow2 = pow2 * 2 % MOD
        print(ans)

    cnt = s.count('1')
    if cnt == n or cnt == 0:
        print(0)
        return
    
    k = s.find('1')
    if k == 0:
        k = s.find('0')
        l = s.find('1', k)
    else:
        l = s.find('0', k)
    
    # print(l, k)
    l = max(2 * k - l, 0) if l >= 0 else 0
    # print(l, k)
    res = 0
    for i in range(k, n):
        res *= 2
        res %= MOD
        if s[i] != s[l]:
            res += 1
        l += 1
        # # if i < k:
        # #     ans[i] = '0'
        # #     continue

        # c = s[i]
        # # if cnt:
        # chk = False
        # # for j in range(1, k + 1):
        # #     if not v[j]:
        # #         continue
        #     # print(j, ans[i-j])
        # q = []
        # replace = len(v) > 1
        # for j in v:
        #     if s[i-j] != c:
        #         if replace:
        #             q.append(j)
        #         if not chk:
        #             res += pow(2, n - i - 1, MOD)
        #             res %= MOD
        #             chk = True
        #         # ans[i] = '1'
        #         # break
        # if replace:
        #     v = q
        # # if chk:
        # #     # for j in range(1, k + 1):
        # #     #     if not v[j]:
        # #     #         continue
        # #     #     if s[i-j] == c:
        # #     #         v[j] = False
        # #     #         cnt -= 1
        # #     res += pow(2, n - i - 1, MOD)
        # #     res %= MOD
        # #     if len(v) > 1:
        # #         q = []
        # #         for j in v:
        # #             if s[i-j] != c:
        # #                 q.append(j)
        # #         v = q
        # # else:
        # #     ans[i] = '0'
        # # else:
        # #     break

    # printAns("".join(ans), k)
    print(res)

t = int(input())
for _ in range(t):
    solve()