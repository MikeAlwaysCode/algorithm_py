#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode.cn/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (37.10%)
# Likes:    2157
# Dislikes: 0
# Total Accepted:    347.5K
# Total Submissions: 936.7K
# Testcase Example:  '"(()"'
#
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
# 
# 
# 示例 2：
# 
# 
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
# 
# 
# 示例 3：
# 
# 
# 输入：s = ""
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# s[i] 为 '(' 或 ')'
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        maxLen = 0
        # Count
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxLen = max(maxLen, 2 * right)
            elif right > left:
                left = right = 0
                
        left = right = 0
        for c in s[::-1]:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxLen = max(maxLen, 2 * right)
            elif right < left:
                left = right = 0
        return maxLen

        '''
        # Stack
        stk = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    maxLen = max(maxLen, i - stk[-1])
        return maxLen
        '''
        '''
        # DP
        n = len(s)
        dp = [0]*n
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
                maxLen = max(maxLen, dp[i]);
        '''
        return maxLen
# @lc code=end

