#
# @lc app=leetcode.cn id=1031 lang=python3
#
# [1031] 两个非重叠子数组的最大和
#
# https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
#
# algorithms
# Medium (59.65%)
# Likes:    189
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 19K
# Testcase Example:  '[0,6,5,2,2,5,1,9,4]\n1\n2'
#
# 给你一个整数数组 nums 和两个整数 firstLen 和 secondLen，请你找出并返回两个非重叠 子数组 中元素的最大和，长度分别为
# firstLen 和 secondLen 。
# 
# 长度为 firstLen 的子数组可以出现在长为 secondLen 的子数组之前或之后，但二者必须是不重叠的。
# 
# 子数组是数组的一个 连续 部分。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
# 输出：20
# 解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
# 输出：29
# 解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
# 输出：31
# 解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= firstLen, secondLen <= 1000
# 2 <= firstLen + secondLen <= 1000
# firstLen + secondLen <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# 
# 
#
from itertools import accumulate
from typing import List


# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        ans = s1 = s2 = 0
        mx1 = [0] * len(nums)
        mx2 = [0] * len(nums)
        for i, x in enumerate(nums):
            s1 += x
            s2 += x
            if i >= firstLen:
                s1 -= nums[i - firstLen]
                ans = max(ans, s1 + mx2[i - firstLen])
            if i >= firstLen - 1:
                mx1[i] = max(mx1[i - 1], s1)
            if i >= secondLen:
                s2 -= nums[i - secondLen]
                ans = max(ans, s2 + mx1[i - secondLen])
            if i >= secondLen - 1:
                mx2[i] = max(mx2[i - 1], s2)
        return ans
# @lc code=end

