import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    s = input().strip()
    nums = []
    plus = substract = 0
    for c in s:
        if c == "+":
            plus += 1
        elif c == "-":
            substract += 1
        else:
            nums.append(c)
    nums.sort(reverse = True)
    m = len(nums)
    i = m - plus - substract
    ans = "".join(nums[:i])
    while i < m:
        if m - i - 1 < substract:
            ans += "-" + nums[i]
        else:
            ans += "+" + nums[i]
        i += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()