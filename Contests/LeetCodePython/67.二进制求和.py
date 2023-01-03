#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode.cn/problems/add-binary/description/
#
# algorithms
# Easy (53.42%)
# Likes:    927
# Dislikes: 0
# Total Accepted:    293.7K
# Total Submissions: 550K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
# 
# 
# 
# 示例 1：
# 
# 
# 输入:a = "11", b = "1"
# 输出："100"
# 
# 示例 2：
# 
# 
# 输入：a = "1010", b = "1011"
# 输出："10101"
# 
# 
# 
# 提示：
# 
# 
# 1 <= a.length, b.length <= 10^4
# a 和 b 仅由字符 '0' 或 '1' 组成
# 字符串如果不是 "0" ，就不含前导零
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return '{0:b}'.format(int(a, 2) + int(b, 2))
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
# @lc code=end

