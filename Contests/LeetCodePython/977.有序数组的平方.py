#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
# https://leetcode.cn/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (68.93%)
# Likes:    594
# Dislikes: 0
# Total Accepted:    378.5K
# Total Submissions: 549.1K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]
# 
# 示例 2：
# 
# 
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 10^4
# -10^4 
# nums 已按 非递减顺序 排序
# 
# 
# 
# 
# 进阶：
# 
# 
# 请你设计时间复杂度为 O(n) 的算法解决本问题
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 1. 平方后直接排序
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(logn)
        # return sorted(num * num for num in nums)

        # 2. 划分为负数降序子数组和正数升序子数组，归并排序
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        negative = -1
        for i, num in enumerate(nums):
            if num < 0:
                negative = i
            else:
                break
        ans = list()
        i, j = negative, negative + 1
        while i >= 0 or j < n:
            if i < 0:
                ans.append(nums[j] * nums[j])
                j += 1
            elif j == n:
                ans.append(nums[i] * nums[i])
                i -= 1
            elif nums[i] * nums[i] < nums[j] * nums[j]:
                ans.append(nums[i] * nums[i])
                i -= 1
            else:
                ans.append(nums[j] * nums[j])
                j += 1
        return ans
        '''
        n = len(nums)
        i,j,k = 0,n - 1,n - 1
        ans = [-1] * n
        while i <= j:
            lm = nums[i] ** 2
            rm = nums[j] ** 2
            if lm > rm:
                ans[k] = lm
                i += 1
            else:
                ans[k] = rm
                j -= 1
            k -= 1
        return ans
        '''
# @lc code=end

