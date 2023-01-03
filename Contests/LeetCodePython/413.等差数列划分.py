#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#
# https://leetcode.cn/problems/arithmetic-slices/description/
#
# algorithms
# Medium (69.52%)
# Likes:    490
# Dislikes: 0
# Total Accepted:    110K
# Total Submissions: 158.2K
# Testcase Example:  '[1,2,3,4]'
#
# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
# 
# 
# 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
# 
# 
# 
# 
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
# 
# 子数组 是数组中的一个连续序列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,4]
# 输出：3
# 解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -1000 
# 
# 
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        left = 0
        ans = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                ans += i - left - 1
            else:
                left = i - 1
        return ans
# @lc code=end

