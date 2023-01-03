#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode.cn/problems/ugly-number-ii/description/
#
# algorithms
# Medium (58.82%)
# Likes:    1011
# Dislikes: 0
# Total Accepted:    146.6K
# Total Submissions: 249.3K
# Testcase Example:  '10'
#
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
# 
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)
# @lc code=end

