#
# @lc app=leetcode.cn id=6131 lang=python3
#
# [6131] 不可能得到的最短骰子序列
#
from typing import *

# @lc code=start
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        s = set()
        
        ans = 0
        for r in rolls:
            s.add(r)
            if len(s) == k:
                ans += 1
                s.clear()
        
        return ans+1
# @lc code=end

sol = Solution()
rolls = [4,2,1,2,3,3,2,4,1]
k = 4
print(sol.shortestSequence(rolls, k))

