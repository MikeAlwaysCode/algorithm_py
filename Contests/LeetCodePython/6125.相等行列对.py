#
# @lc app=leetcode.cn id=6125 lang=python3
#
# [6125] 相等行列对
#
from typing import *
# @lc code=start
import numpy
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        n = len(grid)

        trans = numpy.transpose(grid)

        ans = 0
        for i in range(n):
            for j in range(n):
                if (grid[i] == trans[j]).all():
                    ans += 1
        return(ans)
        '''
        ct = Counter(tuple(row) for row in grid)
        return sum(ct[col] for col in zip(*grid))
# @lc code=end

