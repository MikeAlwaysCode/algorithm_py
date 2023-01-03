#
# @lc app=leetcode.cn id=1802 lang=python3
#
# [1802] 有界数组中指定下标处的最大值
#
# https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/description/
#
# algorithms
# Medium (29.17%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    6.6K
# Total Submissions: 22.5K
# Testcase Example:  '4\n2\n6'
#
# 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
# 
# 
# nums.length == n
# nums[i] 是 正整数 ，其中 0 <= i < n
# abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
# nums 中所有元素之和不超过 maxSum
# nums[index] 的值被 最大化
# 
# 
# 返回你所构造的数组中的 nums[index] 。
# 
# 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 4, index = 2,  maxSum = 6
# 输出：2
# 解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
# 
# 
# 示例 2：
# 
# 输入：n = 6, index = 1,  maxSum = 10
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= maxSum <= 10^9
# 0 <= index < n
# 
# 
#

# @lc code=start
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def cals(x: int) -> int:
            lmn = max(1, x - index) # x往左边递减，最小值是1 or x - index
            rmn = max(1, x - n + index + 1)  # x往右边递减，最小值是1 or x - (n - index - 1)
            # 左半段1 ~ x的和是(x + lmn) * (x - lmn + 1) // 2
            # 右半估x ~ 1的和是(x + rmn) * (x - rmn + 1) // 2
            # x重复算了一次，
            # 两段总长(x - lmn + 1) + (x - rmn + 1) - 1 = x * 2 - lmn - rmn + 1，若两段总长小于n，则剩余部分需要补1
            return (x + lmn) * (x - lmn + 1) // 2 + (x + rmn) * (x - rmn + 1) // 2 + n + lmn + rmn - x * 3 - 1

        # maxSum >= n，故l至少为1
        l, r = 1, maxSum
        while l < r:
            mid = l + r + 1 >> 1
            curs = cals(mid)
            if curs <= maxSum:
                l = mid
            else:
                r = mid - 1
        return l
# @lc code=end

