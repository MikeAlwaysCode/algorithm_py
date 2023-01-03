#
# @lc app=leetcode.cn id=6129 lang=python3
#
# [6129] 全 0 子数组的数目
#

# @lc code=start
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for n in nums:
            if n:
                ans += (count + 1) * count // 2
                count = 0
            else:
                count += 1
                
        ans += (count + 1) * count // 2
        # for n in nums:
        #     if n:
        #         count = 0
        #     else:
        #         count += 1
        #         ans += count
                
        return ans
# @lc code=end

