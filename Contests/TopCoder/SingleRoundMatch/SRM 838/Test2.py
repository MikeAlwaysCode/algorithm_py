from functools import reduce
from math import lcm, gcd
from collections import Counter, defaultdict
from sortedcontainers import SortedSet, SortedList
from typing import List

class PreInPostOrder:
    def reconstruct(self, PIP, IPP):
        

        return 0

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        print("uf initial:")
        print(uf.parent)
        print(uf.rank)
        for num in nums:
            print("============")
            print("Num:", num)
            i = 2
            while i * i <= num:
                if num % i == 0:
                    print("i:", i)
                    print("uf before merge:")
                    print(uf.parent)
                    print(uf.rank)
                    uf.merge(num, i)
                    uf.merge(num, num // i)
                    print("uf after merge:")
                    print(uf.parent)
                    print(uf.rank)
                i += 1
        
        print("uf at last:")
        print(uf.parent)
        print(uf.rank)
        return max(Counter(uf.find(num) for num in nums).values())

def main():
    # sol = Solution()

    # arr = [40,10,20,30]
    # print(sol.arrayRankTransform(arr))
    # nums = [2,3,6,7,4,12,21,39]
    # print(sol.largestComponentSize(nums))

    PIP = {0,1,3,5,4,2}
    IPP = {0,2,3,5,4,1}
    sol = PreInPostOrder()
    print(sol.reconstruct(PIP, IPP))

if __name__ == '__main__':
    main()