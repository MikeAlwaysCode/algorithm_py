#
# @lc app=leetcode.cn id=2659 lang=python3
#
# [2659] 将数组清空
#
# https://leetcode.cn/problems/make-array-empty/description/
#
# algorithms
# Hard (37.88%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 5.3K
# Testcase Example:  '[3,4,-1]'
#
# 给你一个包含若干 互不相同 整数的数组 nums ，你需要执行以下操作 直到数组为空 ：
# 
# 
# 如果数组中第一个元素是当前数组中的 最小值 ，则删除它。
# 否则，将第一个元素移动到数组的 末尾 。
# 
# 
# 请你返回需要多少个操作使 nums 为空。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,4,-1]
# 输出：5
# 
# 
# 
# 
# 
# Operation
# Array
# 
# 
# 
# 
# 1
# [4, -1, 3]
# 
# 
# 2
# [-1, 3, 4]
# 
# 
# 3
# [3, 4]
# 
# 
# 4
# [4]
# 
# 
# 5
# []
# 
# 
# 
# 
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,4,3]
# 输出：5
# 
# 
# 
# 
# 
# Operation
# Array
# 
# 
# 
# 
# 1
# [2, 4, 3]
# 
# 
# 2
# [4, 3]
# 
# 
# 3
# [3, 4]
# 
# 
# 4
# [4]
# 
# 
# 5
# []
# 
# 
# 
# 
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,2,3]
# 输出：3
# 
# 
# 
# 
# 
# Operation
# Array
# 
# 
# 
# 
# 1
# [2, 3]
# 
# 
# 2
# [3]
# 
# 
# 3
# []
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums 中的元素 互不相同 。
# 
# 
#
from itertools import pairwise
from typing import List


# @lc code=start
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        ans = n = len(nums)
        id = sorted(range(n), key = lambda x: nums[x])
        for k, (pre, i) in enumerate(pairwise(id), 1):
            if i < pre:
                ans += n - k
        return ans
# @lc code=end

