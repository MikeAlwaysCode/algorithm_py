import bisect
import copy
import itertools
import math
import string
from collections import Counter, defaultdict, deque
from functools import cache, reduce
from graphlib import TopologicalSorter
from heapq import heapify, heappop, heappush, heapreplace
from itertools import accumulate
from math import gcd, inf, lcm
from operator import *
from typing import List, Optional

from sortedcontainers import SortedList, SortedSet


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.map = dict()

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.e = [0] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n
    
    def findset(self, x: int) -> int:
        # if self.parent[x] == x:
        #     return x
        # self.parent[x] = self.findset(self.parent[x])
        # return self.parent[x]
        cur = x
        while x != self.parent[x]:
            x = self.parent[x]
        if cur != x:
            self.parent[cur] = x
        return x
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.e[x] += 1
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y

class BIT:
    def __init__(self, n: int):
        self.nums = [0] * (n + 1)
        self.n = n
        self.BITree = [0] * (self.n + 1)
        
    def lowbit(self, x: int) -> int:
        return x & -x
    
    def query(self, x: int) -> int:
        ans = 0
        while x:
            ans += self.BITree[x]
            x -= self.lowbit(x)
        return ans

    def add(self, x: int, val: int):
        while x <= self.n:
            self.BITree[x] += val
            x += self.lowbit(x)

    def update(self, x: int, val: int) -> None:
        self.add(x + 1, val - self.nums[x])
        self.nums[x] = val

class Node:
    def __init__(self, l, r):
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        self.v = -1

class SegmentTree:
    def __init__(self):
        self.root = Node(1, int(1e9))

    def modify(self, l, r, v, node=None):
        if l > r:
            return
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            node.v = max(node.v, v)
            return
        self.pushdown(node)
        if l <= node.mid:
            self.modify(l, r, v, node.left)
        if r > node.mid:
            self.modify(l, r, v, node.right)
        self.pushup(node)

    def query(self, l, r, node=None):
        if l > r:
            return 0
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            return node.v
        self.pushdown(node)
        v = -1
        if l <= node.mid:
            v = max(v, self.query(l, r, node.left))
        if r > node.mid:
            v = max(v, self.query(l, r, node.right))
        return v

    def pushup(self, node):
        node.v = max(node.left.v, node.right.v)

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.l, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.r)

class Solution:
    
    def test():
        return
   
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        valid = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    valid[i] |= 1 << j
                    valid[j] |= 1 << i
        @cache
        def dfs(i, state):
            if state == (1 << n) - 1:
                return 1
            res = 0
            for j in range(n):
                if state & (1 << j) or (i != -1 and not valid[i] & (1 << j)): continue
                res = (res + dfs(j, state | (1 << j))) % MOD
            return res
        
        return dfs(-1, 0) % MOD

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(n, -1, -1):
                if dp[j] == math.inf: continue
                t = min(j + time[i] + 1, n)
                dp[t] = min(dp[t], dp[j] + cost[i])
                
        return dp[n]


def main():
    sol = Solution()

    cost = [1,2,3,2]
    time = [1,2,3,2]
    print(sol.paintWalls(cost, time))

    # nums1 = [4,3,1,2]
    # nums2 = [2,4,9,5]
    # queries = [[4,1],[1,3],[2,5]]
    # print(sol.maximumSumQueries(nums1, nums2, queries))

    # nums = [20,1,15]
    # x = 5
    # print(sol.minCost(nums, x))
    
    # mat = [[4,-1,-5],[1,-6,-6],[8,2,3],[3,-3,-7],[7,-5,1],[4,-6,7],[4,2,7]]
    # print(sol.maxIncreasingCells(mat))

    # mat = [[3,1],[3,4]]
    # print(sol.maxIncreasingCells(mat))

    # mat = [[3,1,6],[-9,5,7]]
    # print(sol.maxIncreasingCells(mat))

    # mat = [[2,-4,2,-2,6]]
    # print(sol.maxIncreasingCells(mat))

    # n = 46
    # print(sol.punishmentNumber(n))

    # print(sol.rampartDefensiveLine(rampart))

    # rampart = [[0,3],[4,5],[7,9]]
    # print(sol.rampartDefensiveLine(rampart))

    # maze = [".....","##S..","...#.","T.#..","###.."]
    # print(sol.challengeOfTheKeeper(maze))

    # parents = [-1,0,0,1,2,2]
    # print(sol.evolutionaryRecord(parents))

    # parents = [-1,0,0,2]
    # print(sol.evolutionaryRecord(parents))

    # parents = [-1,0,1,0,3,1,5,1,4,1,2,0,0,11,5,4,4,6,16,2]
    # print(sol.evolutionaryRecord(parents))

if __name__ == '__main__':
    main()