#
# @lc app=leetcode.cn id=1799 lang=python3
#
# [1799] N 次操作后的最大分数和
#
# https://leetcode.cn/problems/maximize-score-after-n-operations/description/
#
# algorithms
# Hard (54.31%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 8.4K
# Testcase Example:  '[1,2]'
#
# 给你 nums ，它是一个大小为 2 * n 的正整数数组。你必须对这个数组执行 n 次操作。
# 
# 在第 i 次操作时（操作编号从 1 开始），你需要：
# 
# 
# 选择两个元素 x 和 y 。
# 获得分数 i * gcd(x, y) 。
# 将 x 和 y 从 nums 中删除。
# 
# 
# 请你返回 n 次操作后你能获得的分数和最大为多少。
# 
# 函数 gcd(x, y) 是 x 和 y 的最大公约数。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2]
# 输出：1
# 解释：最优操作是：
# (1 * gcd(1, 2)) = 1
# 
# 
# 示例 2：
# 
# 输入：nums = [3,4,6,8]
# 输出：11
# 解释：最优操作是：
# (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
# 
# 
# 示例 3：
# 
# 输入：nums = [1,2,3,4,5,6]
# 输出：14
# 解释：最优操作是：
# (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 7
# nums.length == 2 * n
# 1 <= nums[i] <= 10^6
# 
# 
#
import itertools
import math
from typing import List


# @lc code=start
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        d = dict()
        for i in range(n):
            for j in range(i + 1, n):
                d[(nums[i], nums[j])] = math.gcd(nums[i], nums[j])
                d[(nums[j], nums[i])] = d[(nums[i], nums[j])]
        
        s = set()
        ans = 0
        for comb in itertools.combinations(range(n), n // 2):
            if comb in s:
                continue
            left = []
            cs = set(comb)
            for i in range(n):
                if i not in cs:
                    left.append(i)
            s.add(comb)
            s.add(tuple(left))
            for per in itertools.permutations(comb):
                g = []
                for i, j in enumerate(per):
                    g.append(d[(nums[left[i]], nums[j])])
                g.sort()
                ans = max(ans, sum(i * k for i, k in enumerate(g, 1)))
        return ans
# @lc code=end

