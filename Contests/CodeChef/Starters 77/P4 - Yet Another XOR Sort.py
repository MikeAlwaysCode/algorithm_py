import collections
import math
import random
import sys
from functools import *
from heapq import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    arr = ints()
    
    ans = []
    idx = sorted(range(n), key = lambda x: arr[x])
    # print(idx)
    
    def swap(pos: list):
        for i in pos:
            ans.append((i, len(pos)))
            ans.append(pos)
        ans.append((pos[0], len(pos)))
        ans.append(pos)

    d = dict()
    for i in range(n):
        d[idx[i]] = i
        
    flag = [False] * n
    for i in range(n):
        if not flag[i]:
            j = i
            pos = []
            while not flag[j]:
                flag[j] = True
                pos.append(j + 1)
                j = d[j]
            if len(pos) > 1:
                swap(pos)

    '''
    cnt = 0
    ans = []
    def swap2(i: int, j: int):
        arr[i] ^= arr[j]
        arr[j] ^= arr[i]
        arr[i] ^= arr[j]
        ans.append((i + 1, 2))
        ans.append((i + 1, j + 1))
        ans.append((j + 1, 2))
        ans.append((i + 1, j + 1))
        ans.append((i + 1, 2))
        ans.append((i + 1, j + 1))

    def swap3(i: int, j: int, k: int):
        arr[i] ^= arr[j] ^ arr[k]
        arr[j] ^= arr[i] ^ arr[k]
        arr[k] ^= arr[i] ^ arr[j]
        arr[i] ^= arr[j] ^ arr[k]
        ans.append((i + 1, 3))
        ans.append((i + 1, j + 1, k + 1))
        ans.append((j + 1, 3))
        ans.append((i + 1, j + 1, k + 1))
        ans.append((k + 1, 3))
        ans.append((i + 1, j + 1, k + 1))
        ans.append((i + 1, 3))
        ans.append((i + 1, j + 1, k + 1))
    
    for i in range(n):
        l = -1
        for j in range(i + 1, n):
            if arr[j] < arr[i] and (l == -1 or arr[j] < arr[l]):
                l = j
        
        if l == -1: continue
        if l == i + 1:
            cnt += 3
            swap2(i, l)
        else:
            cnt += 4
            swap3(i, l - 1, l)

    print("====")
    print(*arr)
    '''
    print(len(ans) // 2)
    for a in ans:
        print(*a)

t = int(input())
for _ in range(t):
    solve()