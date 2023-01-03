#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#
# https://leetcode.cn/problems/score-of-parentheses/description/
#
# algorithms
# Medium (63.34%)
# Likes:    345
# Dislikes: 0
# Total Accepted:    25.2K
# Total Submissions: 38.7K
# Testcase Example:  '"()"'
#
# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
# 
# 
# () 得 1 分。
# AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
# (A) 得 2 * A 分，其中 A 是平衡括号字符串。
# 
# 
# 
# 
# 示例 1：
# 
# 输入： "()"
# 输出： 1
# 
# 
# 示例 2：
# 
# 输入： "(())"
# 输出： 2
# 
# 
# 示例 3：
# 
# 输入： "()()"
# 输出： 2
# 
# 
# 示例 4：
# 
# 输入： "(()(()))"
# 输出： 6
# 
# 
# 
# 
# 提示：
# 
# 
# S 是平衡括号字符串，且只含有 ( 和 ) 。
# 2 <= S.length <= 50
# 
# 
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = bal = 0
        for i, c in enumerate(s):
            bal += 1 if c == '(' else -1
            if c == ')' and s[i - 1] == '(':
                ans += 1 << bal
        return ans
        '''
        stk = [0]
        for c in s:
            if c == '(':
                stk.append(0)
            else:
                v = stk.pop()
                stk[-1] += max(2 * v, 1)
        return stk[-1]
        '''
        '''
        n = len(s)
        if n == 2:
            return 1

        bal = 0
        for i, c in enumerate(s):
            bal += 1 if c == '(' else -1
            
            if bal == 0:
                if i == n - 1:
                    return 2 * self.scoreOfParentheses(s[1:-1])
                else:
                    return self.scoreOfParentheses(s[:i+1]) + self.scoreOfParentheses(s[i+1:])
        '''
# @lc code=end

