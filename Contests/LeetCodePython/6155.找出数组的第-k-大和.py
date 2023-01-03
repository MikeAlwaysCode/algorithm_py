#
# @lc app=leetcode.cn id=6155 lang=python3
#
# [6155] 找出数组的第 K 大和
#
# https://leetcode.cn/problems/find-the-k-sum-of-an-array/description/
#
# algorithms
# Hard (28.01%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 3.9K
# Testcase Example:  '[2,4,-2]\n5'
#
# 给你一个整数数组 nums 和一个 正 整数 k 。你可以选择数组的任一 子序列 并且对其全部元素求和。
# 
# 数组的 第 k 大和 定义为：可以获得的第 k 个 最大 子序列和（子序列和允许出现重复）
# 
# 返回数组的 第 k 大和 。
# 
# 子序列是一个可以由其他数组删除某些或不删除元素排生而来的数组，且派生过程不改变剩余元素的顺序。
# 
# 注意：空子序列的和视作 0 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,4,-2], k = 5
# 输出：2
# 解释：所有可能获得的子序列和列出如下，按递减顺序排列：
# - 6、4、4、2、2、0、0、-2
# 数组的第 5 大和是 2 。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,-2,3,4,-10,12], k = 16
# 输出：10
# 解释：数组的第 16 大和是 10 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 <= n <= 10^5
# -10^9 <= nums[i] <= 10^9
# 1 <= k <= min(2000, 2^n)
# 
# 
#
from heapq import heappop, heappush
from typing import List
# @lc code=start
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        tot = 0
        for i, x in enumerate(nums):
            if x >= 0:
                tot += x
            else:
                nums[i] = -x
        nums.sort()
        h = [(0, 0)]
        while k > 1:
            k -= 1
            sub_sum, i = heappop(h)
            if i < len(nums):
                heappush(h, (sub_sum + nums[i], i+1))
                if i:
                    heappush(h, (sub_sum + nums[i] - nums[i-1], i+1))

        return tot - h[0][0]
# @lc code=end

