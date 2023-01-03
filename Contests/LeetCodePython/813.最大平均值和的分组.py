#
# @lc app=leetcode.cn id=813 lang=python3
#
# [813] 最大平均值和的分组
#
# https://leetcode.cn/problems/largest-sum-of-averages/description/
#
# algorithms
# Medium (56.39%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 21.1K
# Testcase Example:  '[9,1,2,3,9]\n3'
#
# 给定数组 nums 和一个整数 k 。我们将给定的数组 nums 分成 最多 k 个相邻的非空子数组 。 分数 由每个子数组内的平均值的总和构成。
# 
# 注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。
# 
# 返回我们所能得到的最大 分数 是多少。答案误差在 10^-6 内被视为是正确的。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [9,1,2,3,9], k = 3
# 输出: 20.00000
# 解释: 
# nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20. 
# 我们也可以把 nums 分成[9, 1], [2], [3, 9]. 
# 这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [1,2,3,4,5,6,7], k = 4
# 输出: 20.50000
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#
from itertools import accumulate
from typing import List
# @lc code=start
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = list(accumulate(nums, initial=0))
        dp = [0.0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = prefix[i] / i
        for j in range(2, k + 1):
            for i in range(n, j - 1, -1):
                for x in range(j - 1, i):
                    dp[i] = max(dp[i], dp[x] + (prefix[i] - prefix[x]) / (i - x))
        return dp[n]
# @lc code=end

