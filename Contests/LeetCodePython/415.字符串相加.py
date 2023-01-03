#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode.cn/problems/add-strings/description/
#
# algorithms
# Easy (54.99%)
# Likes:    634
# Dislikes: 0
# Total Accepted:    238.1K
# Total Submissions: 433K
# Testcase Example:  '"11"\n"123"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
# 
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num1 = "11", num2 = "123"
# 输出："134"
# 
# 
# 示例 2：
# 
# 
# 输入：num1 = "456", num2 = "77"
# 输出："533"
# 
# 
# 示例 3：
# 
# 
# 输入：num1 = "0", num2 = "0"
# 输出："0"
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= num1.length, num2.length <= 10^4
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pre = 0
        i = len(num1) - 1
        j = len(num2) - 1
        ans = ""
        while i >= 0 or j >= 0:
            c = pre
            if i >= 0:
                c += int(num1[i])
                i -= 1
            if j >= 0:
                c += int(num2[j])
                j -= 1
            pre = 1 if c > 9 else 0
            ans = str(c%10) + ans
        if pre:
            ans = "1" + ans
        return ans
# @lc code=end

