#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode.cn/problems/multiply-strings/description/
#
# algorithms
# Medium (44.68%)
# Likes:    1085
# Dislikes: 0
# Total Accepted:    267.9K
# Total Submissions: 599.8K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 
# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 
# 示例 2:
# 
# 
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 
# 
# 
# 提示：
# 
# 
# 1 <= num1.length, num2.length <= 200
# num1 和 num2 只能由数字组成。
# num1 和 num2 都不包含任何前导零，除了数字0本身。
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0": #处理特殊情况
            return "0"
        
        l1, l2 = len(num1), len(num2) 
        if l1 < l2: 
            num1, num2 = num2, num1 #保障num1始终比num2大
            l1, l2 = l2, l1
            
        num2 = num2[::-1]
        res = "0"
        for i, digit in enumerate(num2):
            tmp = self.StringMultiplyDigit(num1, int(digit)) + "0" * i #计算num1和num2的当前位的乘积
            res = self.StringPlusString(res, tmp) #计算res和tmp的和

        return res
    
    def StringMultiplyDigit(self,string, n):
        #这个函数的功能是：计算一个字符串和一个整数的乘积，返回字符串
        #举例：输入为 "123", 3， 返回"369"
        s = string[::-1]
        res = []
        for i, char in enumerate(s):
            num = int(char)
            res.append(num * n)
        res = self.CarrySolver(res)
        res = res[::-1]
        return "".join(str(x) for x in res)
        
    def CarrySolver(self, nums):  
        #这个函数的功能是：将输入的数组中的每一位处理好进位
        #举例：输入[15, 27, 12], 返回[5, 8, 4, 1]
        i = 0
        while i < len(nums):
            if nums[i] >= 10:
                carrier = nums[i] // 10
                if i == len(nums) - 1:
                    nums.append(carrier)
                else:
                    nums[i + 1] += carrier
                nums[i] %= 10
            i += 1
                    
        return nums
    
    def StringPlusString(self, s1, s2):
        #这个函数的功能是：计算两个字符串的和。 
        #举例：输入为“123”， “456”, 返回为"579"
        #PS：LeetCode415题就是要写这个函数
        l1, l2 = len(s1), len(s2)
        if l1 < l2:
            s1, s2 = s2, s1
            l1, l2 = l2, l1
        s1 = [int(x) for x in s1]
        s2 = [int(x) for x in s2]
        s1, s2 = s1[::-1], s2[::-1]
        for i, digit in enumerate(s2):
            s1[i] += s2[i]
            
        s1 = self.CarrySolver(s1)
        s1 = s1[::-1]
        return "".join(str(x) for x in s1)
# @lc code=end

