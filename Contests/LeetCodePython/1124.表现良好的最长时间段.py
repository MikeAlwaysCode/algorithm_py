#
# @lc app=leetcode.cn id=1124 lang=python3
#
# [1124] 表现良好的最长时间段
#
# https://leetcode.cn/problems/longest-well-performing-interval/description/
#
# algorithms
# Medium (34.75%)
# Likes:    282
# Dislikes: 0
# Total Accepted:    23.2K
# Total Submissions: 65.1K
# Testcase Example:  '[9,9,6,0,6,6,9]'
#
# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
# 
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
# 
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
# 
# 请你返回「表现良好时间段」的最大长度。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。
# 
# 示例 2：
# 
# 
# 输入：hours = [6,6,6]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= hours.length <= 10^4
# 0 <= hours[i] <= 16
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        s = [0] * (n + 1)  # 前缀和
        st = [0]  # s[0]
        for j, h in enumerate(hours, 1):
            s[j] = s[j - 1] + (1 if h > 8 else -1)
            if s[j] < s[st[-1]]: st.append(j)  # 感兴趣的 j
        ans = 0
        for i in range(n, 0, -1):
            while st and s[i] > s[st[-1]]:
                ans = max(ans, i - st.pop())  # [st[-1],i) 可能是最长子数组
        return ans
# @lc code=end

