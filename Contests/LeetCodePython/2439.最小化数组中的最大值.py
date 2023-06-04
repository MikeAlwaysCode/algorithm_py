#
# @lc app=leetcode.cn id=2439 lang=python3
#
# [2439] 最小化数组中的最大值
#
# https://leetcode.cn/problems/minimize-maximum-of-array/description/
#
# algorithms
# Medium (38.73%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 15.7K
# Testcase Example:  '[3,7,1,6]'
#
# 给你一个下标从 0 开始的数组 nums ，它含有 n 个非负整数。
# 
# 每一步操作中，你需要：
# 
# 
# 选择一个满足 1 <= i < n 的整数 i ，且 nums[i] > 0 。
# 将 nums[i] 减 1 。
# 将 nums[i - 1] 加 1 。
# 
# 
# 你可以对数组执行 任意 次上述操作，请你返回可以得到的 nums 数组中 最大值 最小 为多少。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [3,7,1,6]
# 输出：5
# 解释：
# 一串最优操作是：
# 1. 选择 i = 1 ，nums 变为 [4,6,1,6] 。
# 2. 选择 i = 3 ，nums 变为 [4,6,2,5] 。
# 3. 选择 i = 1 ，nums 变为 [5,5,2,5] 。
# nums 中最大值为 5 。无法得到比 5 更小的最大值。
# 所以我们返回 5 。
# 
# 
# 示例 2：
# 
# 输入：nums = [10,1]
# 输出：10
# 解释：
# 最优解是不改动 nums ，10 是最大值，所以返回 10 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 2 <= n <= 10^5
# 0 <= nums[i] <= 10^9
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        pre = tot = 0
        for i in range(0, n):
            tot += nums[i]
            pre = max(pre, (tot + i) // (i + 1))
        return pre
# @lc code=end

