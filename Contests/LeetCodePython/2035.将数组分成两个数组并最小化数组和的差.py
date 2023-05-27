#
# @lc app=leetcode.cn id=2035 lang=python3
#
# [2035] 将数组分成两个数组并最小化数组和的差
#
# https://leetcode.cn/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/
#
# algorithms
# Hard (34.52%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 11.3K
# Testcase Example:  '[3,9,7,3]'
#
# 给你一个长度为 2 * n 的整数数组。你需要将 nums 分成 两个 长度为 n 的数组，分别求出两个数组的和，并 最小化 两个数组和之 差的绝对值
# 。nums 中每个元素都需要放入两个数组之一。
# 
# 请你返回 最小 的数组和之差。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：nums = [3,9,7,3]
# 输出：2
# 解释：最优分组方案是分成 [3,9] 和 [7,3] 。
# 数组和之差的绝对值为 abs((3 + 9) - (7 + 3)) = 2 。
# 
# 
# 示例 2：
# 
# 输入：nums = [-36,36]
# 输出：72
# 解释：最优分组方案是分成 [-36] 和 [36] 。
# 数组和之差的绝对值为 abs((-36) - (36)) = 72 。
# 
# 
# 示例 3：
# 
# 
# 
# 输入：nums = [2,-1,0,4,-2,-9]
# 输出：0
# 解释：最优分组方案是分成 [2,4,-9] 和 [-1,0,-2] 。
# 数组和之差的绝对值为 abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 15
# nums.length == 2 * n
# -10^7 <= nums[i] <= 10^7
# 
# 
#
import bisect
import math
from typing import List


# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        res = [[] for _ in range(n + 1)]
        for mask in range(1 << n):
            s = 0
            for i in range(n):
                if mask >> i & 1:
                    s += nums[i]
                else:
                    s -= nums[i]
            res[mask.bit_count()].append(s)

        for i in range(n + 1): res[i].sort()

        ans = math.inf
        for mask in range(1 << n):
            s = 0
            for i in range(n, n * 2):
                if mask >> (i - n) & 1:
                    s += nums[i]
                else:
                    s -= nums[i]
            cnt = mask.bit_count()
            j = bisect.bisect(res[cnt], s)
            if j: ans = min(ans, s - res[cnt][j - 1])
            if j < len(res[cnt]): ans = min(ans, res[cnt][j] - s)
        return ans
# @lc code=end

