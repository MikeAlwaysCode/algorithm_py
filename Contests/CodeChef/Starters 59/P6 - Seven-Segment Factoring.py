import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    digDis = [
            [1, 2, 3, 4, 5, 6],     # 0
            [2, 3],                 # 1
            [1, 2, 4, 5, 7],        # 2 -
            [1, 2, 3, 4, 7],        # 3
            [2, 3, 6, 7],           # 4
            [1, 3, 4, 6, 7],        # 5 -
            [1, 3, 4, 5, 6, 7],     # 6 -
            [1, 2, 3],              # 7
            [1, 2, 3, 4, 5, 6, 7],  # 8
            [1, 2, 3, 4, 6, 7]      # 9
            ]

    arr = ints()
    n = arr[0]
    digSum = [0] * 10
    for i in range(10):
        for j in digDis[i]:
            digSum[i] += arr[j]

    ans = digSum[1]
    if digSum[2] < ans and n % 2 == 0:
        ans = digSum[2]
    if digSum[5] < ans and n % 5 == 0:
        ans = digSum[5]
    if digSum[6] < ans and n % 6 == 0:
        ans = digSum[6]
    '''
    if digSum[6] < digSum[1] and digSum[6] < digSum[2]:
        q = [(6, digSum[6])]
        while q:
            tmp = q
            q = []
            for x, xs in tmp:
                if xs + digSum[5] < ans:
                    nx = int("5" + str(x))
                    if n % nx == 0:
                        ans = xs + digSum[5]
                    else:
                        q.append((nx, xs + digSum[5]))
                if xs + digSum[6] < ans:
                    nx = int("6" + str(x))
                    if n % nx == 0:
                        ans = xs + digSum[6]
                    else:
                        q.append((nx, xs + digSum[6]))
    '''
    def cal(x) -> int:
        res = 0
        while x:
            res += digSum[x%10]
            x //= 10
        return res
    for i in range(1, 9):
        for mask in range(2 ** i):
            num = 0
            for j in range(i):
                num *= 10
                if mask & (1 << j):
                    num += 5
                else:
                    num += 6
            num *= 10
            num += 6
            if n % num == 0:
                ans = min(ans, cal(num))

    print(ans)

t = int(input())
for _ in range(t):
    solve()