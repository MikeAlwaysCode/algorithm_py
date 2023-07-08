#
# @lc app=leetcode.cn id=1830 lang=python3
#
# [1830] 使字符串有序的最少操作次数
#
# https://leetcode.cn/problems/minimum-number-of-operations-to-make-string-sorted/description/
#
# algorithms
# Hard (53.03%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 2.8K
# Testcase Example:  '"cba"'
#
# 给你一个字符串 s （下标从 0 开始）。你需要对 s 执行以下操作直到它变为一个有序字符串：
# 
# 
# 找到 最大下标 i ，使得 1 <= i < s.length 且 s[i] < s[i - 1] 。
# 找到 最大下标 j ，使得 i <= j < s.length 且对于所有在闭区间 [i, j] 之间的 k 都有 s[k] < s[i - 1]
# 。
# 交换下标为 i - 1​​​​ 和 j​​​​ 处的两个字符。
# 将下标 i 开始的字符串后缀反转。
# 
# 
# 请你返回将字符串变成有序的最少操作次数。由于答案可能会很大，请返回它对 10^9 + 7 取余 的结果。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "cba"
# 输出：5
# 解释：模拟过程如下所示：
# 操作 1：i=2，j=2。交换 s[1] 和 s[2] 得到 s="cab" ，然后反转下标从 2 开始的后缀字符串，得到 s="cab" 。
# 操作 2：i=1，j=2。交换 s[0] 和 s[2] 得到 s="bac" ，然后反转下标从 1 开始的后缀字符串，得到 s="bca" 。
# 操作 3：i=2，j=2。交换 s[1] 和 s[2] 得到 s="bac" ，然后反转下标从 2 开始的后缀字符串，得到 s="bac" 。
# 操作 4：i=1，j=1。交换 s[0] 和 s[1] 得到 s="abc" ，然后反转下标从 1 开始的后缀字符串，得到 s="acb" 。
# 操作 5：i=2，j=2。交换 s[1] 和 s[2] 得到 s="abc" ，然后反转下标从 2 开始的后缀字符串，得到 s="abc" 。
# 
# 
# 示例 2：
# 
# 输入：s = "aabaa"
# 输出：2
# 解释：模拟过程如下所示：
# 操作 1：i=3，j=4。交换 s[2] 和 s[4] 得到 s="aaaab" ，然后反转下标从 3 开始的后缀字符串，得到 s="aaaba" 。
# 操作 2：i=4，j=4。交换 s[3] 和 s[4] 得到 s="aaaab" ，然后反转下标从 4 开始的后缀字符串，得到 s="aaaab" 。
# 
# 
# 示例 3：
# 
# 输入：s = "cdbea"
# 输出：63
# 
# 示例 4：
# 
# 输入：s = "leetcodeleetcodeleetcode"
# 输出：982157772
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 3000
# s​ 只包含小写英文字母。
# 
# 
#

# @lc code=start
class Solution:
    def makeStringSorted(self, s: str) -> int:
        mod = 10**9 + 7
        
        # 快速幂，用来计算 x^y mod m
        def quickmul(x: int, y: int) -> int:
            # Python 有方便的内置函数
            return pow(x, y, mod)
    
        n = len(s)
        
        # fac[i] 表示 i! mod m
        # facinv[i] 表示 i! 在 mod m 意义下的乘法逆元
        fac, facinv = [0] * (n + 1), [0] * (n + 1)
        fac[0] = facinv[0] = 1
        for i in range(1, n):
            fac[i] = fac[i - 1] * i % mod
            # 使用费马小定理 + 快速幂计算乘法逆元
            facinv[i] = quickmul(fac[i], mod - 2)
        
        # freq 存储每个字符出现的次数
        freq = collections.Counter(s)
        
        ans = 0
        for i in range(n - 1):
            # rank 求出比 s[i] 小的字符数量
            rank = sum(occ for ch, occ in freq.items() if ch < s[i])
            # 排列个数的分子
            cur = rank * fac[n - i - 1] % mod
            # 依次乘分母每一项阶乘的乘法逆元
            for ch, occ in freq.items():
                cur = cur * facinv[occ] % mod
            
            ans += cur
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                freq.pop(s[i])
        
        return ans % mod
# @lc code=end

