#
# @lc app=leetcode.cn id=2640 lang=python3
#
# [2640] 一个数组所有前缀的分数
#
# https://leetcode.cn/problems/find-the-score-of-all-prefixes-of-an-array/description/
#
# algorithms
# Medium (80.46%)
# Likes:    3
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 4.9K
# Testcase Example:  '[2,3,7,5,10]'
#
# 定义一个数组 arr 的 转换数组 conver 为：
# 
# 
# conver[i] = arr[i] + max(arr[0..i])，其中 max(arr[0..i]) 是满足 0 <= j <= i 的所有
# arr[j] 中的最大值。
# 
# 
# 定义一个数组 arr 的 分数 为 arr 转换数组中所有元素的和。
# 
# 给你一个下标从 0 开始长度为 n 的整数数组 nums ，请你返回一个长度为 n 的数组 ans ，其中 ans[i]是前缀 nums[0..i]
# 的分数。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,3,7,5,10]
# 输出：[4,10,24,36,56]
# 解释：
# 对于前缀 [2] ，转换数组为 [4] ，所以分数为 4 。
# 对于前缀 [2, 3] ，转换数组为 [4, 6] ，所以分数为 10 。
# 对于前缀 [2, 3, 7] ，转换数组为 [4, 6, 14] ，所以分数为 24 。
# 对于前缀 [2, 3, 7, 5] ，转换数组为 [4, 6, 14, 12] ，所以分数为 36 。
# 对于前缀 [2, 3, 7, 5, 10] ，转换数组为 [4, 6, 14, 12, 20] ，所以分数为 56 。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,1,2,4,8,16]
# 输出：[2,4,8,16,32,64]
# 解释：
# 对于前缀 [1] ，转换数组为 [2] ，所以分数为 2 。
# 对于前缀 [1, 1]，转换数组为 [2, 2] ，所以分数为 4 。
# 对于前缀 [1, 1, 2]，转换数组为 [2, 2, 4] ，所以分数为 8 。
# 对于前缀 [1, 1, 2, 4]，转换数组为 [2, 2, 4, 8] ，所以分数为 16 。
# 对于前缀 [1, 1, 2, 4, 8]，转换数组为 [2, 2, 4, 8, 16] ，所以分数为 32 。
# 对于前缀 [1, 1, 2, 4, 8, 16]，转换数组为 [2, 2, 4, 8, 16, 32] ，所以分数为 64 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 
# 
#
from itertools import accumulate
from typing import List



# @lc code=start
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        mx = 0
        for i, x in enumerate(nums):
            mx = max(mx, x)
            nums[i] += mx
        return list(accumulate(nums))
# @lc code=end

