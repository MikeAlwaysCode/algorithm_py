#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#
# https://leetcode.cn/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (36.89%)
# Likes:    311
# Dislikes: 0
# Total Accepted:    43.4K
# Total Submissions: 117.8K
# Testcase Example:  '12'
#
# 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
# 
# 注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 12
# 输出：21
# 
# 
# 示例 2：
# 
# 
# 输入：n = 21
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            return -1

        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]
        ans = int(''.join(nums))
        return ans if ans < 2 ** 31 else -1
# @lc code=end

