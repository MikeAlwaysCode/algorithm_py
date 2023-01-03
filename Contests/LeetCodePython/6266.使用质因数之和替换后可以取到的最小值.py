#
# @lc app=leetcode.cn id=6266 lang=python3
#
# [6266] 使用质因数之和替换后可以取到的最小值
#
# https://leetcode.cn/problems/smallest-value-after-replacing-with-sum-of-prime-factors/description/
#
# algorithms
# Medium (45.65%)
# Likes:    5
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 7.6K
# Testcase Example:  '15'
#
# 给你一个正整数 n 。
# 
# 请你将 n 的值替换为 n 的 质因数 之和，重复这一过程。
# 
# 
# 注意，如果 n 能够被某个质因数多次整除，则在求和时，应当包含这个质因数同样次数。
# 
# 
# 返回 n 可以取到的最小值。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 15
# 输出：5
# 解释：最开始，n = 15 。
# 15 = 3 * 5 ，所以 n 替换为 3 + 5 = 8 。
# 8 = 2 * 2 * 2 ，所以 n 替换为 2 + 2 + 2 = 6 。
# 6 = 2 * 3 ，所以 n 替换为 2 + 3 = 5 。
# 5 是 n 可以取到的最小值。
# 
# 
# 示例 2：
# 
# 输入：n = 3
# 输出：3
# 解释：最开始，n = 3 。
# 3 是 n 可以取到的最小值。
# 
# 
# 
# 提示：
# 
# 
# 2 <= n <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            s = 0
            d = 2
            x = n
            while d * d <= x:
                while x % d == 0:
                    s += d
                    x //= d
                d += 1
            if x > 1: s += x
            if n == s:
                return n
            n = s
        '''
        mxn = n
        factor = [1] * (mxn + 1)
        primes = list()
        
        for i in range(2, mxn + 1):
            if factor[i] != 1:
                continue
            primes.append(i)
            for j in range(i, mxn + 1, i):
                factor[j] = i

        def prime_factor(x) -> int:
            # res = set()
            res = 0
            while x != 1:
                # res.add(factor[x])
                res += factor[x]
                x //= factor[x]
            return res

        ps = prime_factor(n)
        while ps != n:
            n = ps
            ps = prime_factor(n)

        return n
        '''
# @lc code=end

