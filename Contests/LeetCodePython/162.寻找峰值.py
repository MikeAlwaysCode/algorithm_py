#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
# https://leetcode.cn/problems/find-peak-element/description/
#
# algorithms
# Medium (49.47%)
# Likes:    920
# Dislikes: 0
# Total Accepted:    267.6K
# Total Submissions: 540.8K
# Testcase Example:  '[1,2,3,1]'
#
# 峰值元素是指其值严格大于左右相邻值的元素。
# 
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
# 
# 你可以假设 nums[-1] = nums[n] = -∞ 。
# 
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,1,3,5,6,4]
# 输出：1 或 5 
# 解释：你的函数可以返回索引 1，其峰值元素为 2；
# 或者返回索引 5， 其峰值元素为 6。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# 对于所有有效的 i 都有 nums[i] != nums[i + 1]
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # 辅助函数，输入下标 i，返回 nums[i] 的值
        # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]
        
        left, right, ans = 0, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
# @lc code=end

