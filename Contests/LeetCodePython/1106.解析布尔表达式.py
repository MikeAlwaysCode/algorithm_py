#
# @lc app=leetcode.cn id=1106 lang=python3
#
# [1106] 解析布尔表达式
#
# https://leetcode.cn/problems/parsing-a-boolean-expression/description/
#
# algorithms
# Hard (58.79%)
# Likes:    124
# Dislikes: 0
# Total Accepted:    13.4K
# Total Submissions: 20.2K
# Testcase Example:  '"&(|(f))"'
#
# 给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。
# 
# 有效的表达式需遵循以下约定：
# 
# 
# "t"，运算结果为 True
# "f"，运算结果为 False
# "!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
# "&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
# "|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）
# 
# 
# 
# 
# 示例 1：
# 
# 输入：expression = "!(f)"
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：expression = "|(f,t)"
# 输出：true
# 
# 
# 示例 3：
# 
# 输入：expression = "&(t,f)"
# 输出：false
# 
# 
# 示例 4：
# 
# 输入：expression = "|(&(t,f,t),!(t))"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= expression.length <= 20000
# expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。
# expression 是以上述形式给出的有效表达式，表示一个布尔值。
# 
# 
#

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        sign = []
        for c in expression:
            if c == '!' or c == '|' or c == '&':
                sign.append(c)
            elif c == '(' or c == 'f' or c == 't':
                stk.append(c)
            elif c == ')':
                if sign[-1] == '!':
                    res = 't' if stk[-1] == 'f' else 'f'
                    stk.pop()
                else:
                    fchk = tchk = False
                    while stk[-1] != '(':
                        p = stk.pop()
                        if p == 'f':
                            fchk = True
                        elif p == 't':
                            tchk = True
                    if sign[-1] == '|':
                        if tchk:
                            res = 't'
                        else:
                            res = 'f'
                    else:
                        if fchk:
                            res = 'f'
                        else:
                            res = 't'
                sign.pop()
                stk.pop()
                stk.append(res)
        return True if stk[-1] == 't' else False
# @lc code=end

