#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode.cn/problems/contains-duplicate/description/
#
# algorithms
# Easy (55.74%)
# Likes:    805
# Dislikes: 0
# Total Accepted:    647.5K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,1]'
#
# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,1]
# 输出：true
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,4]
# 输出：false
# 
# 示例 3：
# 
# 
# 输入：nums = [1,1,1,3,3,4,3,2,4,2]
# 输出：true
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
# @lc code=end

