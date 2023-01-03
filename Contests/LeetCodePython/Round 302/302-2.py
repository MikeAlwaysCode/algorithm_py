#
# @lc app=leetcode.cn id=6131 lang=python3
#
# [6131] 不可能得到的最短骰子序列
#
from typing import *
import numpy

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        trans = numpy.transpose(grid)

        ans = 0
        for i in range(n):
            for j in range(n):
                if (grid[i] == trans[j]).all():
                    ans += 1
        return(ans)
# @lc code=end

sol = Solution()
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(sol.equalPairs(grid))
grid = [[3,2,1],[1,7,6],[2,7,7]]
print(sol.equalPairs(grid))

