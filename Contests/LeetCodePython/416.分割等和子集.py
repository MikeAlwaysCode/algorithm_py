#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode.cn/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (52.25%)
# Likes:    1658
# Dislikes: 0
# Total Accepted:    378.4K
# Total Submissions: 724.3K
# Testcase Example:  '[1,5,11,5]'
#
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target & 1:
            return False
        target //= 2
        dp = [False] * (target + 1)
        dp[0] = True
        for x in nums:
            for j in range(target, x - 1, -1):
                dp[j] |= dp[j - x]
        return dp[target]
# @lc code=end

