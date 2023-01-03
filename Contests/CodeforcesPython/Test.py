from functools import reduce
from math import lcm, gcd
from collections import Counter, defaultdict
from sortedcontainers import SortedSet, SortedList
from typing import List

class Solution:
    def solve(t: int) -> None:
        n=int(input())
        l=list(map(int,input().split()))
        dicta={}
        for i in range(n):
            dicta[l[i]]=0
        ret=0
        for i in range(n-1,-1,-1):
            dicta[l[i]]+=1
            if(dicta[l[i]]>1):
                ret=i+1
                break
        print(ret)

def main():
    sol = Solution()

    t = int(input())

    for _ in range(t):
        sol.solve()

if __name__ == '__main__':
    main()