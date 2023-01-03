#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#
# https://leetcode.cn/problems/delete-and-earn/description/
#
# algorithms
# Medium (62.48%)
# Likes:    703
# Dislikes: 0
# Total Accepted:    88.7K
# Total Submissions: 142K
# Testcase Example:  '[3,4,2]'
#
# 给你一个整数数组 nums ，你可以对它进行一些操作。
# 
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i]
# + 1 的元素。
# 
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
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
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        n = len(cnt)
        # dp[i][0]表示不选择第i个数字，dp[i][1]表示选择第i个数字
        dp = [[0] * 2 for _ in range(n)]
        for i, (k, v) in enumerate(sorted(cnt.items())):
            if i == 0:
                dp[i][1] = k * v
            else:
                # 不选择当前数字，则直接等于前面的较大值
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
                if k != prek + 1:
                    # 选择当前数字，假设前一个数+1不等于当前数字，则可以从前一个数字选或不选转移过来取较大值
                    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + k * v
                else:
                    # 否则只能从前一个数字不选转移过来
                    dp[i][1] = dp[i - 1][0] + k * v
            prek = k
        # print(dp)
        return max(dp[n - 1])
# @lc code=end

