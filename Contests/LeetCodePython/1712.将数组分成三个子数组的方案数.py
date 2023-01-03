#
# @lc app=leetcode.cn id=1712 lang=python3
#
# [1712] 将数组分成三个子数组的方案数
#
# https://leetcode.cn/problems/ways-to-split-array-into-three-subarrays/description/
#
# algorithms
# Medium (27.95%)
# Likes:    91
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 42K
# Testcase Example:  '[1,1,1]'
#
# 我们称一个分割整数数组的方案是 好的 ，当它满足：
# 
# 
# 数组被分成三个 非空 连续子数组，从左至右分别命名为 left ， mid ， right 。
# left 中元素和小于等于 mid 中元素和，mid 中元素和小于等于 right 中元素和。
# 
# 
# 给你一个 非负 整数数组 nums ，请你返回 好的 分割 nums 方案数目。由于答案可能会很大，请你将结果对 10^9 + 7 取余后返回。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,1]
# 输出：1
# 解释：唯一一种好的分割方案是将 nums 分成 [1] [1] [1] 。
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,2,2,5,0]
# 输出：3
# 解释：nums 总共有 3 种好的分割方案：
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [3,2,1]
# 输出：0
# 解释：没有好的分割方案。
# 
# 
# 
# 提示：
# 
# 
# 3 
# 0 
# 
# 
#
import bisect
from itertools import accumulate
from typing import List


# @lc code=start
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        pres = list(accumulate(nums))
        ans = 0
        i, j, k = 0, 1, 1
        while i < n - 2 and pres[i] * 3 <= pres[-1]:
            j = max(i + 1, j)
            while j < n - 1 and pres[j] < pres[i] * 2:
                j += 1
                
            while k < n - 2 and pres[k + 1] * 2 <= pres[i] + pres[-1]:
                k += 1

            if k >= j:
                ans += k - j + 1
                ans %= MOD

            i += 1
        '''
        for i in range(n - 2):
            left = pres[i]
            if left * 3 > pres[-1]:
                break

            j = bisect.bisect_left(pres, pres[i] * 2, i + 1)
            k = bisect.bisect(pres, (pres[-1] + pres[i]) // 2, i + 1, n - 1)
            if k >= n or pres[k] * 2 > (pres[i] + pres[-1]):
                k -= 1

            ans += k - j + 1
            ans %= MOD
        '''
        return ans
# @lc code=end

