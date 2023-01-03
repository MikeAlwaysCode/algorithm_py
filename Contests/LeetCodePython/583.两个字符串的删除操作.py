#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#
# https://leetcode.cn/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (65.88%)
# Likes:    507
# Dislikes: 0
# Total Accepted:    102.5K
# Total Submissions: 155.6K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
# 
# 每步 可以删除任意一个字符串中的一个字符。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: word1 = "sea", word2 = "eat"
# 输出: 2
# 解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
# 
# 
# 示例  2:
# 
# 
# 输入：word1 = "leetcode", word2 = "etco"
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 1 <= word1.length, word2.length <= 500
# word1 和 word2 只包含小写英文字母
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        
        return dp[m][n]
        '''
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        lcs = dp[m][n]
        return m - lcs + n - lcs
        '''
# @lc code=end

