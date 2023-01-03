#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#
# https://leetcode.cn/problems/solve-the-equation/description/
#
# algorithms
# Medium (44.16%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    16.1K
# Total Submissions: 36.4K
# Testcase Example:  '"x+5-3+x=6+x-2"'
#
# 求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。
# 
# 如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。
# 
# 如果方程中只有一个解，要保证返回值 'x' 是一个整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: equation = "x+5-3+x=6+x-2"
# 输出: "x=2"
# 
# 
# 示例 2:
# 
# 
# 输入: equation = "x=x"
# 输出: "Infinite solutions"
# 
# 
# 示例 3:
# 
# 
# 输入: equation = "2x=x"
# 输出: "x=0"
# 
# 
# 
# 
# 
# 
# 提示:
# 
# 
# 3 <= equation.length <= 1000
# equation 只有一个 '='.
# equation 方程由整数组成，其绝对值在 [0, 100] 范围内，不含前导零和变量 'x' 。 ​​​
# 
# 
#

# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        xn, dn, factor, turn, preNum = 0, 0, 1, 1, "0"
        for x in equation:
            if x.isdigit():
                preNum += x
            elif x == 'x':
                if preNum == "0":
                    k = 1
                else:
                    k = int(preNum)
                xn += factor * turn * k
                preNum = "0"
            else:
                dn += factor * turn * int(preNum)
                preNum = "0"
                if x == '=':
                    factor = 1
                    turn = -1
                elif x == '+':
                    factor = 1
                elif x == '-':
                    factor = -1
        if preNum != "0":
            dn += factor * turn * int(preNum)
        dn *= -1
        # print(xn, dn)
        if xn == 0:
            if dn == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            # return "x=" + str(dn // xn)
            return f"x={-dn // xn}"
# @lc code=end

