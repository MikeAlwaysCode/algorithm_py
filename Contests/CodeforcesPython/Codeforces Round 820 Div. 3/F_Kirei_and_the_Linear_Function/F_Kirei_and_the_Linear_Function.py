from bisect import bisect
import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    s = input().strip()
    w, m = map(int, input().split())
    query = []
    for _ in range(m):
        l, r, k = map(int, input().split())
        query.append((l, r, k))

    n = len(s)
    # md = [0] * n
    cnt = [0] * 9
    count = 0
    d = [[] for _ in range(9)]
    ps = [0] * (n + 1)
    for i in range(n):
        ps[i+1] = (ps[i] + int(s[i])) % 9
    for i in range(n - w + 1):
        d[(ps[i+w] - ps[i]) % 9].append(i)
    # for i in range(n - w + 1):
    #     # md[i] = int(s[i:i + w]) % 9
    #     md = int(s[i:i + w]) % 9
    #     if cnt[md] < 2:
    #         d[md].append(i+1)
    #         cnt[md] += 1
    #         if cnt[md] >= 2:
    #             count += 1
    #             if count >= 9:
    #                 break

    # for dl in d:
    #     dl.sort()
    # # print(d)

    for q in query:
        # v = int(s[q[0]-1:q[1]]) % 9
        v = (ps[q[1]] - ps[q[0]-1]) % 9
        k = q[2]

        ans = []
        for i in range(9):
            if not d[i]:
                continue

            j = (k - i * v % 9) % 9
            if j == i:
                if len(d[i]) >= 2:
                    ans.append((d[i][0] + 1, d[i][1] + 1))
                continue
            if not d[j]:
                continue

            ans.append((d[i][0] + 1, d[j][0] + 1))
        if ans:
            ans.sort()
            print(*ans[0])
        else:
            print(-1, -1)
        '''
        l1 = l2 = -1
        # print("v:", v)
        for j in range(n - w):
            k = (query[i][2] - md[j] * v % 9) % 9
            # print("k:", k, "--", j)
            # if not d[k] or d[k][-1] <= j:
            if not d[k]:
                continue
            # l = bisect(d[k], j)
            for dl in d[k]:
                if dl != j:
                    l2 = dl + 1
                    break
            if l2 != -1:
                l1 = min(j + 1, l2)
                l2 = max(j + 1, l2)
                break
        print(l1, l2)
        '''

t = int(input())
for _ in range(t):
    solve()