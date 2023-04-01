#
# @lc app=leetcode.cn id=1092 lang=python3
#
# [1092] 最短公共超序列
#
# https://leetcode.cn/problems/shortest-common-supersequence/description/
#
# algorithms
# Hard (54.26%)
# Likes:    143
# Dislikes: 0
# Total Accepted:    7.2K
# Total Submissions: 12.6K
# Testcase Example:  '"abac"\n"cab"'
#
# 给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。
# 
# （如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，那么 S 就是 T
# 的子序列）
# 
# 
# 
# 示例：
# 
# 输入：str1 = "abac", str2 = "cab"
# 输出："cabac"
# 解释：
# str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。 
# str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
# 最终我们给出的答案是满足上述属性的最短字符串。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= str1.length, str2.length <= 1000
# str1 和 str2 都由小写英文字母组成。
# 
# 
#

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0] = list(range(m + 1))
        for i in range(1, n + 1):
            dp[i][0] = i
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1]) + 1

        ans = []
        i, j = n - 1, m - 1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                ans.append(s[i])
                i -= 1
                j -= 1
            elif dp[i + 1][j + 1] == dp[i][j + 1] + 1:
                ans.append(s[i])
                i -= 1
            else:
                ans.append(t[j])
                j -= 1
        return s[:i + 1] + t[:j + 1] + "".join(reversed(ans))
# @lc code=end

