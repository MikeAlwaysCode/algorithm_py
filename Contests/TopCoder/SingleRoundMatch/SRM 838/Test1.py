from functools import reduce
from math import lcm, gcd
from collections import Counter, defaultdict
from sortedcontainers import SortedSet, SortedList
from typing import List

class FlippingCoinSum:
    def flip(self, faceUp, faceDown, goal):
        nope = -123456789
        tot = sum(faceUp)
        if tot == goal:
            return tuple()
        upa = list(faceUp)
        upd = list(faceDown)
        upa.sort()
        upd.sort()

        n = len(faceUp)
        m = len(faceDown)
        
        dp = [False] * (1 << n)
        dp[0] = True
        cursum = [0] * (1 << n)
        for i in range(0, 1 << n):
            if not dp[i]:
                continue
            for j in range(n):
                if cursum[i] + nums[j] > per:
                    break
                if (i >> j & 1) == 0:
                    next = i | (1 << j)
                    if not dp[next]:
                        cursum[next] = (cursum[i] + nums[j]) % per
                        dp[next] = True
        return dp[(1 << n) - 1]

def main():
    a = (2, 2, 5)
    b = (1, 10)
    goal = 14
    sol = FlippingCoinSum()
    print(sol.flip(a, b, goal))

if __name__ == '__main__':
    main()