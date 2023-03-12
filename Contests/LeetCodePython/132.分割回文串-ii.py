#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# https://leetcode.cn/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (49.88%)
# Likes:    651
# Dislikes: 0
# Total Accepted:    73.3K
# Total Submissions: 146.9K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
# 
# 返回符合要求的 最少分割次数 。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a"
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：s = "ab"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由小写英文字母组成
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[False] * n for _ in range(n)]
        for i in range(n):
            g[i][i] = True
            for j in range(i - 1, -1, -1):
                if s[j] == s[i] and (i - j - 1 == 0 or g[j + 1][i - 1]):
                    g[j][i] = True
        # print(g)
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if g[0][i]:
                dp[i + 1] = 0
                continue

            for j in range(i + 1):
                if g[j][i]:
                    dp[i+1] = min(dp[i+1], dp[j] + 1)
        # print(dp)
        return dp[n]
# @lc code=end

