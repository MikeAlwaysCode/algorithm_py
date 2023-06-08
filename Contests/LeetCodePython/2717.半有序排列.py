#
# @lc app=leetcode.cn id=2717 lang=python3
#
# [2717] 半有序排列
#
# https://leetcode.cn/problems/semi-ordered-permutation/description/
#
# algorithms
# Easy (73.12%)
# Likes:    1
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 6.2K
# Testcase Example:  '[2,1,4,3]'
#
# 给你一个下标从 0 开始、长度为 n 的整数排列 nums 。
# 
# 如果排列的第一个数字等于 1 且最后一个数字等于 n ，则称其为 半有序排列 。你可以执行多次下述操作，直到将 nums 变成一个 半有序排列
# ：
# 
# 
# 选择 nums 中相邻的两个元素，然后交换它们。
# 
# 
# 返回使 nums 变成 半有序排列 所需的最小操作次数。
# 
# 排列 是一个长度为 n 的整数序列，其中包含从 1 到 n 的每个数字恰好一次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,1,4,3]
# 输出：2
# 解释：可以依次执行下述操作得到半有序排列：
# 1 - 交换下标 0 和下标 1 对应元素。排列变为 [1,2,4,3] 。
# 2 - 交换下标 2 和下标 3 对应元素。排列变为 [1,2,3,4] 。
# 可以证明，要让 nums 成为半有序排列，不存在执行操作少于 2 次的方案。
# 
# 示例 2：
# 
# 
# 输入：nums = [2,4,1,3]
# 输出：3
# 解释：
# 可以依次执行下述操作得到半有序排列：
# 1 - 交换下标 1 和下标 2 对应元素。排列变为 [2,1,4,3] 。
# 2 - 交换下标 0 和下标 1 对应元素。排列变为 [1,2,4,3] 。
# 3 - 交换下标 2 和下标 3 对应元素。排列变为 [1,2,3,4] 。
# 可以证明，要让 nums 成为半有序排列，不存在执行操作少于 3 次的方案。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,3,4,2,5]
# 输出：0
# 解释：这个排列已经是一个半有序排列，无需执行任何操作。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length == n <= 50
# 1 <= nums[i] <= 50
# nums 是一个 排列
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(1)
        j = nums.index(n)
        return i + n - 1 - j - (i > j)
# @lc code=end

