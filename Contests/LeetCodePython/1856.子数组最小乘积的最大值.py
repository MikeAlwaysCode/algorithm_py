#
# @lc app=leetcode.cn id=1856 lang=python3
#
# [1856] 子数组最小乘积的最大值
#
# https://leetcode.cn/problems/maximum-subarray-min-product/description/
#
# algorithms
# Medium (37.40%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    9.4K
# Total Submissions: 25.1K
# Testcase Example:  '[1,2,3,2]'
#
# 一个数组的 最小乘积 定义为这个数组中 最小值 乘以 数组的 和 。
# 
# 
# 比方说，数组 [3,2,5] （最小值是 2）的最小乘积为 2 * (3+2+5) = 2 * 10 = 20 。
# 
# 
# 给你一个正整数数组 nums ，请你返回 nums 任意 非空子数组 的最小乘积 的 最大值 。由于答案可能很大，请你返回答案对  10^9 + 7 取余
# 的结果。
# 
# 请注意，最小乘积的最大值考虑的是取余操作 之前 的结果。题目保证最小乘积的最大值在 不取余 的情况下可以用 64 位有符号整数 保存。
# 
# 子数组 定义为一个数组的 连续 部分。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,2]
# 输出：14
# 解释：最小乘积的最大值由子数组 [2,3,2] （最小值是 2）得到。
# 2 * (2+3+2) = 2 * 7 = 14 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,3,3,1,2]
# 输出：18
# 解释：最小乘积的最大值由子数组 [3,3] （最小值是 3）得到。
# 3 * (3+3) = 3 * 6 = 18 。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [3,1,5,6,4,2]
# 输出：60
# 解释：最小乘积的最大值由子数组 [5,6,4] （最小值是 4）得到。
# 4 * (5+6+4) = 4 * 15 = 60 。
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
from itertools import accumulate
from typing import List


# @lc code=start
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pres = list(accumulate(nums, initial = 0))
        
        left, right, stk = [0] * n, [n] * n, []
        for i, x in enumerate(nums):
            while stk and nums[stk[-1]] >= x:
                right[stk.pop()] = i
            if stk: left[i] = stk[-1] + 1
            stk.append(i)
        return max((pres[right[i]] - pres[left[i]]) * x for i, x in enumerate(nums)) % (10 ** 9 + 7)
# @lc code=end

