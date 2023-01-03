#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#
# https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/description/
#
# algorithms
# Medium (74.57%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    54.7K
# Total Submissions: 74.9K
# Testcase Example:  '"())"'
#
# 只有满足下面几点之一，括号字符串才是有效的：
# 
# 
# 它是一个空字符串，或者
# 它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
# 它可以被写作 (A)，其中 A 是有效字符串。
# 
# 
# 给定一个括号字符串 s ，移动N次，你就可以在字符串的任何位置插入一个括号。
# 
# 
# 例如，如果 s = "()))" ，你可以插入一个开始括号为 "(()))" 或结束括号为 "())))" 。
# 
# 
# 返回 为使结果字符串 s 有效而必须添加的最少括号数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "())"
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：s = "((("
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 只包含 '(' 和 ')' 字符。
# 
# 
#
from collections import deque
# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = cnt = 0
        for c in s:
            if c == "(":
                cnt += 1
            elif cnt:
                cnt -= 1
            else:
                ans += 1
        ans += cnt
        return ans
        '''
        ans = 0
        q = deque()
        for c in s:
            if c == "(":
                q.append(c)
            elif q:
                q.pop()
            else:
                ans += 1
        ans += len(q)
        return ans
        '''
# @lc code=end

