#
# @lc app=leetcode.cn id=1249 lang=python3
#
# [1249] 移除无效的括号
#
# https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/description/
#
# algorithms
# Medium (59.05%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    38.4K
# Total Submissions: 65.1K
# Testcase Example:  '"lee(t(c)o)de)"'
#
# 给你一个由 '('、')' 和小写字母组成的字符串 s。
# 
# 你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。
# 
# 请返回任意一个合法字符串。
# 
# 有效「括号字符串」应当符合以下 任意一条 要求：
# 
# 
# 空字符串或只包含小写字母的字符串
# 可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
# 可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "lee(t(c)o)de)"
# 输出："lee(t(c)o)de"
# 解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a)b(c)d"
# 输出："ab(c)d"
# 
# 
# 示例 3：
# 
# 
# 输入：s = "))(("
# 输出：""
# 解释：空字符串也是有效的
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s[i] 可能是 '('、')' 或英文小写字母
# 
# 
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)
# @lc code=end

