#
# @lc app=leetcode.cn id=592 lang=python3
#
# [592] 分数加减运算
#
# https://leetcode.cn/problems/fraction-addition-and-subtraction/description/
#
# algorithms
# Medium (58.51%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    12.2K
# Total Submissions: 20.9K
# Testcase Example:  '"-1/2+1/2"'
#
# 给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。 
# 
# 这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为
# 2/1。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: expression = "-1/2+1/2"
# 输出: "0/1"
# 
# 
# 示例 2:
# 
# 
# 输入: expression = "-1/2+1/2+1/3"
# 输出: "1/3"
# 
# 
# 示例 3:
# 
# 
# 输入: expression = "1/3-1/2"
# 输出: "-1/6"
# 
# 
# 
# 
# 提示:
# 
# 
# 输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。 
# 输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。
# 输入只包含合法的最简分数，每个分数的分子与分母的范围是  [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
# 输入的分数个数范围是 [1,10]。
# 最终结果的分子与分母保证是 32 位整数范围内的有效整数。
# 
# 
#
from functools import reduce
from math import lcm, gcd
# @lc code=start
class Solution:
    def fractionAddition(self, expression: str) -> str:
        a = [[] for _ in range(2)]
        
        if expression[0] != '-':
            s = "+" + expression
        else:
            s = expression

        index, sign = 1, 1
        next = True
        for x in s:
            if x == '-':
                sign = -1
                index = (index + 1) & 1
                next = True
            elif x == '+':
                sign = 1
                index = (index + 1) & 1
                next = True
            elif x == '/':
                sign = 1
                index = (index + 1) & 1
                next = True
            else:
                d = int(x)
                if next:
                    a[index].append(sign * d)
                else:
                    a[index][-1] = a[index][-1] * 10 + d
                next = False
        # print(a)
        denominator = reduce(lcm, a[1])
        # print(denominator)
        numerator = 0
        for i in range(len(a[0])):
            numerator += a[0][i] * denominator // a[1][i]

        g = gcd(numerator, denominator)
        if g > 1:
            numerator //= g
            denominator //= g
        
        return str(numerator) + "/" + str(denominator)
# @lc code=end

