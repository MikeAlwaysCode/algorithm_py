#
# @lc app=leetcode.cn id=1015 lang=python3
#
# [1015] 可被 K 整除的最小整数
#
# https://leetcode.cn/problems/smallest-integer-divisible-by-k/description/
#
# algorithms
# Medium (37.07%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    10K
# Total Submissions: 24.2K
# Testcase Example:  '1'
#
# 给定正整数 k ，你需要找出可以被 k 整除的、仅包含数字 1 的最 小 正整数 n 的长度。
# 
# 返回 n 的长度。如果不存在这样的 n ，就返回-1。
# 
# 注意： n 不符合 64 位带符号整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：k = 1
# 输出：1
# 解释：最小的答案是 n = 1，其长度为 1。
# 
# 示例 2：
# 
# 
# 输入：k = 2
# 输出：-1
# 解释：不存在可被 2 整除的正整数 n 。
# 
# 示例 3：
# 
# 
# 输入：k = 3
# 输出：3
# 解释：最小的答案是 n = 111，其长度为 3。
# 
# 
# 
# 提示：
# 
# 
# 1 <= k <= 10^5
# 
# 
#

# @lc code=start
# 计算欧拉函数（n 以内的与 n 互质的数的个数）
def phi(n: int) -> int:
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            res = res // i * (i - 1)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        res = res // n * (n - 1)
    return res

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        m = phi(k * 9)
        # 从小到大枚举不超过 sqrt(m) 的因子
        i = 1
        while i * i <= m:
            if m % i == 0 and pow(10, i, k * 9) == 1:
                return i
            i += 1
        # 从小到大枚举不低于 sqrt(m) 的因子
        i -= 1
        while True:
            if m % i == 0 and pow(10, m // i, k * 9) == 1:
                return m // i
            i -= 1
'''
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        x = 1 % k
        for i in count(1):  # 一定有解
            if x == 0:
                return i
            x = (x * 10 + 1) % k
'''
# @lc code=end

