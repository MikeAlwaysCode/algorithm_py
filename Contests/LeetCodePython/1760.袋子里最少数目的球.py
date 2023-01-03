#
# @lc app=leetcode.cn id=1760 lang=python3
#
# [1760] 袋子里最少数目的球
#
# https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/description/
#
# algorithms
# Medium (58.11%)
# Likes:    99
# Dislikes: 0
# Total Accepted:    9.4K
# Total Submissions: 16.2K
# Testcase Example:  '[9]\n2'
#
# 给你一个整数数组 nums ，其中 nums[i] 表示第 i 个袋子里球的数目。同时给你一个整数 maxOperations 。
# 
# 你可以进行如下操作至多 maxOperations 次：
# 
# 
# 选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 正整数 个球。
# 
# 
# 比方说，一个袋子里有 5 个球，你可以把它们分到两个新袋子里，分别有 1 个和 4 个球，或者分别有 2 个和 3 个球。
# 
# 
# 
# 
# 你的开销是单个袋子里球数目的 最大值 ，你想要 最小化 开销。
# 
# 请你返回进行上述操作后的最小开销。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [9], maxOperations = 2
# 输出：3
# 解释：
# - 将装有 9 个球的袋子分成装有 6 个和 3 个球的袋子。[9] -> [6,3] 。
# - 将装有 6 个球的袋子分成装有 3 个和 3 个球的袋子。[6,3] -> [3,3,3] 。
# 装有最多球的袋子里装有 3 个球，所以开销为 3 并返回 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,4,8,2], maxOperations = 4
# 输出：2
# 解释：
# - 将装有 8 个球的袋子分成装有 4 个和 4 个球的袋子。[2,4,8,2] -> [2,4,4,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,4,4,4,2] -> [2,2,2,4,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,4,4,2] -> [2,2,2,2,2,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2] 。
# 装有最多球的袋子里装有 2 个球，所以开销为 2 并返回 2 。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [7,17], maxOperations = 2
# 输出：7
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
import bisect
from typing import List
# @lc code=start
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 1, nums[-1]
        while l < r:
            mid = l + r >> 1
            cost = 0
            j = bisect.bisect(nums, mid)
            for k in range(j, n):
                cost += (nums[k] - 1) // mid
            if cost > maxOperations:
                l = mid + 1
            else:
                r = mid
        return l
# @lc code=end

