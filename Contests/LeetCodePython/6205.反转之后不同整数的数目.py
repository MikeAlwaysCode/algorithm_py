#
# @lc app=leetcode.cn id=6205 lang=python3
#
# [6205] 反转之后不同整数的数目
#
# https://leetcode.cn/problems/count-number-of-distinct-integers-after-reverse-operations/description/
#
# algorithms
# Medium (74.66%)
# Likes:    2
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 7.6K
# Testcase Example:  '[1,13,10,12,31]'
#
# 给你一个由 正 整数组成的数组 nums 。
# 
# 你必须取出数组中的每个整数，反转其中每个数位，并将反转后得到的数字添加到数组的末尾。这一操作只针对 nums 中原有的整数执行。
# 
# 返回结果数组中 不同 整数的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,13,10,12,31]
# 输出：6
# 解释：反转每个数字后，结果数组是 [1,13,10,12,31,1,31,1,21,13] 。
# 反转后得到的数字添加到数组的末尾并按斜体加粗表示。注意对于整数 10 ，反转之后会变成 01 ，即 1 。
# 数组中不同整数的数目为 6（数字 1、10、12、13、21 和 31）。
# 
# 示例 2：
# 
# 
# 输入：nums = [2,2,2]
# 输出：1
# 解释：反转每个数字后，结果数组是 [2,2,2,2,2,2] 。
# 数组中不同整数的数目为 1（数字 2）。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set(nums) | set(int(str(a)[::-1]) for a in nums))

        '''
        n = len(nums)
        s = set(nums)
        
        def reverse(x: int) -> int:
            nx = 0
            while x:
                nx *= 10
                nx += x % 10
                x //= 10
            return nx
        for a in nums:
            s.add(reverse(a))
        
        return len(s)
        '''
# @lc code=end

