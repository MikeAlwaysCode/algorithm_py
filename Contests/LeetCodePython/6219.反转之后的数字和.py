#
# @lc app=leetcode.cn id=6219 lang=python3
#
# [6219] 反转之后的数字和
#
# https://leetcode.cn/problems/sum-of-number-and-its-reverse/description/
#
# algorithms
# Medium (45.05%)
# Likes:    5
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 12.1K
# Testcase Example:  '443'
#
# 给你一个 非负 整数 num 。如果存在某个 非负 整数 k 满足 k + reverse(k) = num  ，则返回 true ；否则，返回
# false 。
# 
# reverse(k) 表示 k 反转每个数位后得到的数字。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num = 443
# 输出：true
# 解释：172 + 271 = 443 ，所以返回 true 。
# 
# 
# 示例 2：
# 
# 
# 输入：num = 63
# 输出：false
# 解释：63 不能表示为非负整数及其反转后数字之和，返回 false 。
# 
# 
# 示例 3：
# 
# 
# 输入：num = 181
# 输出：true
# 解释：140 + 041 = 181 ，所以返回 true 。注意，反转后的数字可能包含前导零。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= num <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        # def reverse(x: int) -> int:
        #     nx = 0
        #     while x:
        #         nx *= 10
        #         nx += x % 10
        #         x //= 10
        #     return nx
        
        return any(a + int(str(a)[::-1]) == num for a in range(num + 1))
        # for a in range(num+1):
        #     # if a + reverse(a) == num:
        #     if a + int(str(a)[::-1]) == num:
        #         return True
        
        # return False
# @lc code=end

