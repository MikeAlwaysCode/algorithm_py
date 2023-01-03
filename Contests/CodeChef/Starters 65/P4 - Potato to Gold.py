import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush
from typing import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
MOD = 10 ** 9 + 7

def solve() -> None:
    n, k = map(int, input().split())
    arr = ints()

    cnt = Counter(a%k for a in arr)
    # print(cnt)
    ans = 1 + cnt[0]
    if k % 2 == 0 and cnt[k//2]:
        ans = ans * (cnt[k//2] + 1) % MOD
    for i in range(1, (k + 1)//2):
        ans = ans * pow(2, cnt[i], MOD) + ans * pow(2, cnt[k-i], MOD) - ans
        ans %= MOD

    '''
    ans = pow(2, n, MOD)
    print(cnt)
    factors = []
    for i in range(k//2 + 1):
        if cnt[i] <= 0 or (i > 0 and cnt[k-i] <= 0):
            continue
        if i == 0 or i * 2 == k:
            if cnt[i] > 1:
                m = ((pow(2, cnt[i], MOD) - cnt[i] - 1) % MOD)
                factors.append(m)
                m = m * (pow(2, n - cnt[i], MOD) % MOD)
                ans = (ans - m) % MOD
        else:
            m = ((pow(2, cnt[i], MOD) - 1) % MOD) * ((pow(2, cnt[k-i], MOD) - 1) % MOD)
            factors.append(m)
            m = (m * pow(2, n - cnt[i] - cnt[k-i], MOD) % MOD)
            ans = (ans - m) % MOD
    for mask in range(1, 1<<len(factors)):
        # if mask.bit_count() == 1:
        if str(mask).count('1') == 1:
            continue
        bit_cnt = 0
        mul = 1
        for j in range(len(factors)):
            if (mask >> j) & 1:
                mul *= factors[j]
                bit_cnt += 1
        # if bit_cnt == 1:
        #     continue
        if bit_cnt & 1:
            ans = (ans - mul) % MOD
        else:
            ans = (ans + mul) % MOD
    '''
    print(ans)

t = int(input())
for _ in range(t):
    solve()