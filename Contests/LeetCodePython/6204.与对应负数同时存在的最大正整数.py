#
# @lc app=leetcode.cn id=6204 lang=python3
#
# [6204] 与对应负数同时存在的最大正整数
#
# https://leetcode.cn/problems/largest-positive-integer-that-exists-with-its-negative/description/
#
# algorithms
# Easy (71.91%)
# Likes:    0
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 8.3K
# Testcase Example:  '[-1,2,-3,3]'
#
# 给你一个 不包含 任何零的整数数组 nums ，找出自身与对应的负数都在数组中存在的最大正整数 k 。
# 
# 返回正整数 k ，如果不存在这样的整数，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-1,2,-3,3]
# 输出：3
# 解释：3 是数组中唯一一个满足题目要求的 k 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [-1,10,6,7,-7,1]
# 输出：7
# 解释：数组中存在 1 和 7 对应的负数，7 的值更大。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [-10,8,6,7,-2,-3]
# 输出：-1
# 解释：不存在满足题目要求的 k ，返回 -1 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# nums[i] != 0
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        s = set()
        for a in nums:
            if -a in s:
                ans = max(ans, abs(a))
            s.add(a)
        return ans
        '''
        nums.sort()
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            if nums[i] + nums[j] == 0:
                return nums[j]
            if nums[i] + nums[j] < 0:
                i += 1
            else:
                j -= 1
        return -1
        '''
# @lc code=end

