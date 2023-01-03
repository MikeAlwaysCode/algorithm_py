#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#
# https://leetcode.cn/problems/fibonacci-number/description/
#
# algorithms
# Easy (66.62%)
# Likes:    524
# Dislikes: 0
# Total Accepted:    446.4K
# Total Submissions: 670.1K
# Testcase Example:  '2'
#
# 斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
# 
# 
# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
# 
# 
# 给定 n ，请计算 F(n) 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1
# 
# 
# 示例 2：
# 
# 
# 输入：n = 3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2
# 
# 
# 示例 3：
# 
# 
# 输入：n = 4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 30
# 
# 
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = 5**0.5
        fibN = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n
        return round(fibN / sqrt5)

    '''
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        q = [[1, 1], [1, 0]]
        res = self.matrix_pow(q, n - 1)
        return res[0][0]
    
    def matrix_pow(self, a: List[List[int]], n: int) -> List[List[int]]:
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1:
                ret = self.matrix_multiply(ret, a)
            n >>= 1
            a = self.matrix_multiply(a, a)
        return ret

    def matrix_multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c
    '''
    '''
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p, q = q, r
            r = p + q
        
        return r
    '''
# @lc code=end

