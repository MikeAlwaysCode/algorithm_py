#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 可被三整除的最大和
#
# https://leetcode.cn/problems/greatest-sum-divisible-by-three/description/
#
# algorithms
# Medium (52.68%)
# Likes:    247
# Dislikes: 0
# Total Accepted:    24.9K
# Total Submissions: 46.1K
# Testcase Example:  '[3,6,5,1,8]'
#
# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [3,6,5,1,8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
# 
# 示例 2：
# 
# 输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
# 
# 
# 示例 3：
# 
# 输入：nums = [1,2,3,4,4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4
# 
# 
#
import math
from typing import List


# @lc code=start
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [0, -math.inf, -math.inf]
        for x in nums:
            g = f[:]
            for i in range(3):
                g[(i + x) % 3] = max(g[(i + x) % 3], f[i] + x)
            f = g
        return f[0]
        '''
        s = 0
        m = [[] for _ in range(3)]
        for x in nums:
            s += x
            if x % 3: m[x % 3].append(x)
        if s % 3 == 0: return s
        m[1].sort()
        m[2].sort()
        k = s % 3
        ans = 0
        if m[k]: ans = s - m[k][0]
        if len(m[k ^ 3]) > 1: ans = max(ans, s - m[k ^ 3][0] - m[k ^ 3][1])
        return ans
        '''
# @lc code=end

