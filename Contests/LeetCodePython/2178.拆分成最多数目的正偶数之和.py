#
# @lc app=leetcode.cn id=2178 lang=python3
#
# [2178] 拆分成最多数目的正偶数之和
#
# https://leetcode.cn/problems/maximum-split-of-positive-even-integers/description/
#
# algorithms
# Medium (56.45%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    9.7K
# Total Submissions: 16.1K
# Testcase Example:  '12'
#
# 给你一个整数 finalSum 。请你将它拆分成若干个 互不相同 的正偶数之和，且拆分出来的正偶数数目 最多 。
# 
# 
# 比方说，给你 finalSum = 12 ，那么这些拆分是 符合要求 的（互不相同的正偶数且和为 finalSum）：(2 + 10) ，(2 + 4 +
# 6) 和 (4 + 8) 。它们中，(2 + 4 + 6) 包含最多数目的整数。注意 finalSum 不能拆分成 (2 + 2 + 4 + 4)
# ，因为拆分出来的整数必须互不相同。
# 
# 
# 请你返回一个整数数组，表示将整数拆分成 最多 数目的正偶数数组。如果没有办法将 finalSum 进行拆分，请你返回一个 空 数组。你可以按 任意
# 顺序返回这些整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：finalSum = 12
# 输出：[2,4,6]
# 解释：以下是一些符合要求的拆分：(2 + 10)，(2 + 4 + 6) 和 (4 + 8) 。
# (2 + 4 + 6) 为最多数目的整数，数目为 3 ，所以我们返回 [2,4,6] 。
# [2,6,4] ，[6,2,4] 等等也都是可行的解。
# 
# 
# 示例 2：
# 
# 
# 输入：finalSum = 7
# 输出：[]
# 解释：没有办法将 finalSum 进行拆分。
# 所以返回空数组。
# 
# 
# 示例 3：
# 
# 
# 输入：finalSum = 28
# 输出：[6,8,2,12]
# 解释：以下是一些符合要求的拆分：(2 + 26)，(6 + 8 + 2 + 12) 和 (4 + 24) 。
# (6 + 8 + 2 + 12) 有最多数目的整数，数目为 4 ，所以我们返回 [6,8,2,12] 。
# [10,2,4,12] ，[6,2,4,16] 等等也都是可行的解。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= finalSum <= 10^10
# 
# 
#
import math
from typing import List


# @lc code=start
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1: return []
        k = (math.isqrt(4 * finalSum + 1) - 1) // 2
        ans = list(range(2, 2 * k + 1, 2))
        ans[-1] += finalSum - (k + 1) * k
        return ans
        '''
        ans = []
        cur = 2
        while finalSum >= cur:
            ans.append(cur)
            finalSum -= cur
            cur += 2
        ans[-1] += finalSum
        return ans
        '''
# @lc code=end

