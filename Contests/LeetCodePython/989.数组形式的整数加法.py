#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#
# https://leetcode.cn/problems/add-to-array-form-of-integer/description/
#
# algorithms
# Easy (46.59%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    67.3K
# Total Submissions: 144.6K
# Testcase Example:  '[1,2,0,0]\n34'
#
# 整数的 数组形式  num 是按照从左到右的顺序表示其数字的数组。
# 
# 
# 例如，对于 num = 1321 ，数组形式是 [1,3,2,1] 。
# 
# 
# 给定 num ，整数的 数组形式 ，和整数 k ，返回 整数 num + k 的 数组形式 。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num = [1,2,0,0], k = 34
# 输出：[1,2,3,4]
# 解释：1200 + 34 = 1234
# 
# 
# 示例 2：
# 
# 
# 输入：num = [2,7,4], k = 181
# 输出：[4,5,5]
# 解释：274 + 181 = 455
# 
# 
# 示例 3：
# 
# 
# 输入：num = [2,1,5], k = 806
# 输出：[1,0,2,1]
# 解释：215 + 806 = 1021
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= num.length <= 10^4
# 0 <= num[i] <= 9
# num 不包含任何前导零，除了零本身
# 1 <= k <= 10^4
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        ans = []
        carry = 0
        for i in range(n - 1, -1, -1):
            ans.append((num[i] + k % 10 + carry) % 10)
            carry = (num[i] + k % 10 + carry) // 10
            k //= 10
        while k or carry:
            ans.append((k % 10 + carry) % 10)
            carry = (k % 10 + carry) // 10
            k //= 10
        ans.reverse()
        return ans
# @lc code=end

