#
# @lc app=leetcode.cn id=1330 lang=python3
#
# [1330] 翻转子数组得到最大的数组值
#
# https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/description/
#
# algorithms
# Hard (42.36%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    3.7K
# Total Submissions: 7.2K
# Testcase Example:  '[2,3,1,5,4]'
#
# 给你一个整数数组 nums 。「数组值」定义为所有满足 0 <= i < nums.length-1 的 |nums[i]-nums[i+1]| 的和。
# 
# 你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 一次 。
# 
# 请你找到可行的最大 数组值 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,3,1,5,4]
# 输出：10
# 解释：通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值为 10 。
# 
# 
# 示例 2：
# 
# 输入：nums = [2,4,9,24,2,1,10]
# 输出：68
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 3*10^4
# -10^5 <= nums[i] <= 10^5
# 
# 
#
import math
from typing import List


# @lc code=start
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        ans = 0
        mx, mn = 0, math.inf
        n = len(nums)
        r1 = r2 = 0
        for i in range(n - 1):
            ans += abs(nums[i] - nums[i + 1])
            if nums[i] >= nums[i + 1]:
                mx = max(mx, nums[i + 1])
                mn = min(mn, nums[i])
            if nums[i] <= nums[i + 1]:
                mx = max(mx, nums[i])
                mn = min(mn, nums[i + 1])
            r1 = max(r1, abs(nums[i] - nums[-1]) - abs(nums[i] - nums[i + 1]))
            r2 = max(r2, abs(nums[i + 1] - nums[0]) - abs(nums[i] - nums[i + 1]))
        return ans + max(r1, r2, (mx - mn) * 2)
# @lc code=end

