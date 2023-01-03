#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
# https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (52.54%)
# Likes:    647
# Dislikes: 0
# Total Accepted:    237.6K
# Total Submissions: 452.8K
# Testcase Example:  '["2","1","+","3","*"]'
#
# 根据 逆波兰表示法，求表达式的值。
# 
# 有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
# 
# 注意 两个整数之间的除法只保留整数部分。
# 
# 可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：tokens = ["2","1","+","3","*"]
# 输出：9
# 解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
# 
# 
# 示例 2：
# 
# 
# 输入：tokens = ["4","13","5","/","+"]
# 输出：6
# 解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
# 
# 
# 示例 3：
# 
# 
# 输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# 输出：22
# 解释：该算式转化为常见的中缀算术表达式为：
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
# 
# 提示：
# 
# 
# 1 <= tokens.length <= 10^4
# tokens[i] 是一个算符（"+"、"-"、"*" 或 "/"），或是在范围 [-200, 200] 内的一个整数
# 
# 
# 
# 
# 逆波兰表达式：
# 
# 逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。
# 
# 
# 平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
# 该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。
# 
# 
# 逆波兰表达式主要有以下两个优点：
# 
# 
# 去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
# 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中
# 
# 
#
from operator import add, mul, sub
from typing import List
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x, y: int(x / y),   # 需要注意 python 中负数除法的表现与题目不一致
        }

        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)
            
        return stack[0]
        '''
        stk = []
        for s in tokens:
            if s == '+':
                stk.append(stk.pop() + stk.pop())
            elif s == '-':
                b = stk.pop()
                a = stk.pop()
                stk.append(a - b)
            elif s == '*':
                stk.append(stk.pop() * stk.pop())
            elif s == '/':
                b = stk.pop()
                a = stk.pop()
                stk.append(int(a / b))
            else:
                stk.append(int(s))
        return stk[-1]
        '''
# @lc code=end

