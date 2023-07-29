#
# @lc app=leetcode.cn id=1911 lang=python3
#
# [1911] 最大子序列交替和
#
# https://leetcode.cn/problems/maximum-alternating-subsequence-sum/description/
#
# algorithms
# Medium (59.10%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    9.7K
# Total Submissions: 15.2K
# Testcase Example:  '[4,2,5,3]'
#
# 一个下标从 0 开始的数组的 交替和 定义为 偶数 下标处元素之 和 减去 奇数 下标处元素之 和 。
# 
# 
# 比方说，数组 [4,2,5,3] 的交替和为 (4 + 5) - (2 + 3) = 4 。
# 
# 
# 给你一个数组 nums ，请你返回 nums 中任意子序列的 最大交替和 （子序列的下标 重新 从 0 开始编号）。
# 
# 
# 
# 
# 一个数组的 子序列 是从原数组中删除一些元素后（也可能一个也不删除）剩余元素不改变顺序组成的数组。比方说，[2,7,4] 是
# [4,2,3,7,2,1,4] 的一个子序列（加粗元素），但是 [2,4,2] 不是。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [4,2,5,3]
# 输出：7
# 解释：最优子序列为 [4,2,5] ，交替和为 (4 + 5) - 2 = 7 。
# 
# 
# 示例 2：
# 
# 输入：nums = [5,6,7,8]
# 输出：8
# 解释：最优子序列为 [8] ，交替和为 8 。
# 
# 
# 示例 3：
# 
# 输入：nums = [6,2,1,2,4,5]
# 输出：10
# 解释：最优子序列为 [6,1,5] ，交替和为 (6 + 5) - 1 = 10 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans += max(0, nums[i] - nums[i - 1])
        return ans
# @lc code=end

