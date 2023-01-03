#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#
# https://leetcode.cn/problems/monotonic-array/description/
#
# algorithms
# Easy (57.38%)
# Likes:    178
# Dislikes: 0
# Total Accepted:    77.1K
# Total Submissions: 134.4K
# Testcase Example:  '[1,2,2,3]'
#
# 如果数组是单调递增或单调递减的，那么它是 单调 的。
# 
# 如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i]> =
# nums[j]，那么数组 nums 是单调递减的。
# 
# 当给定的数组 nums 是单调数组时返回 true，否则返回 false。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,2,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [6,5,4,4]
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,3,2]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = True
        for i in range(1, len(nums)):
            if inc and nums[i] < nums[i - 1]:
                inc = False
            if dec and nums[i] > nums[i - 1]:
                dec = False
            if not inc and not dec:
                return False
        return True
# @lc code=end

