#
# @lc app=leetcode.cn id=775 lang=python3
#
# [775] 全局倒置与局部倒置
#
# https://leetcode.cn/problems/global-and-local-inversions/description/
#
# algorithms
# Medium (45.79%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    10.9K
# Total Submissions: 23.1K
# Testcase Example:  '[1,0,2]'
#
# 给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。
# 
# 全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：
# 
# 
# 0 
# nums[i] > nums[j]
# 
# 
# 局部倒置 的数目等于满足下述条件的下标 i 的数目：
# 
# 
# 0 
# nums[i] > nums[i + 1]
# 
# 
# 当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,0,2]
# 输出：true
# 解释：有 1 个全局倒置，和 1 个局部倒置。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,0]
# 输出：false
# 解释：有 2 个全局倒置，和 1 个局部倒置。
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 
# 0 
# nums 中的所有整数 互不相同
# nums 是范围 [0, n - 1] 内所有数字组成的一个排列
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(x - i) <= 1 for i, x in enumerate(nums))
        '''
        min_suf = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i - 1] > min_suf:
                return False
            min_suf = min(min_suf, nums[i])
        return True
        '''
# @lc code=end

