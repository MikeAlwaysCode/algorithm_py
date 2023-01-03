#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#
# https://leetcode.cn/problems/partition-array-into-disjoint-intervals/description/
#
# algorithms
# Medium (47.29%)
# Likes:    135
# Dislikes: 0
# Total Accepted:    19K
# Total Submissions: 38.3K
# Testcase Example:  '[5,0,3,8,6]'
#
# 给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得：
# 
# 
# left 中的每个元素都小于或等于 right 中的每个元素。
# left 和 right 都是非空的。
# left 的长度要尽可能小。
# 
# 
# 在完成这样的分组后返回 left 的 长度 。
# 
# 用例可以保证存在这样的划分方法。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,0,3,8,6]
# 输出：3
# 解释：left = [5,0,3]，right = [8,6]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,1,1,0,6,12]
# 输出：4
# 解释：left = [1,1,1,0]，right = [6,12]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^6
# 可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        suff = [0] * n
        for i in range(n-1, -1, -1):
            if i == n - 1:
                suff[i] = nums[i]
            else:
                suff[i] = min(nums[i], suff[i+1])
        mx = 0
        for i in range(n - 1):
            mx = max(mx, nums[i])
            if mx <= suff[i+1]:
                return i + 1
# @lc code=end

