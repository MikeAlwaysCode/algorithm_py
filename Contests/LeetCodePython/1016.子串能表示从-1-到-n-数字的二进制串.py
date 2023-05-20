#
# @lc app=leetcode.cn id=1016 lang=python3
#
# [1016] 子串能表示从 1 到 N 数字的二进制串
#
# https://leetcode.cn/problems/binary-string-with-substrings-representing-1-to-n/description/
#
# algorithms
# Medium (58.31%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    11K
# Total Submissions: 18K
# Testcase Example:  '"0110"\n3'
#
# 给定一个二进制字符串 s 和一个正整数 n，如果对于 [1, n] 范围内的每个整数，其二进制表示都是 s 的 子字符串 ，就返回 true，否则返回
# false 。
# 
# 子字符串 是字符串中连续的字符序列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "0110", n = 3
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "0110", n = 4
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s[i] 不是 '0' 就是 '1'
# 1 <= n <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        '''
        if n == 1:
            return '1' in s

        m = len(s)
        k = n.bit_length() - 1
        if m < max(n - (1 << k) + k + 1, (1 << (k - 1)) + k - 1):
            return False

        # 对于长为 k 的在 [lower, upper] 内的二进制数，判断这些数 s 是否都有
        def check(k: int, lower: int, upper: int) -> bool:
            if lower > upper: return True
            seen = set()
            mask = (1 << (k - 1)) - 1
            x = int(s[:k - 1], 2)
            for c in s[k - 1:]:
                # & mask 可以去掉最高比特位，从而实现滑窗的「出」
                # << 1 | int(c) 即为滑窗的「入」
                x = ((x & mask) << 1) | int(c)
                if lower <= x <= upper:
                    seen.add(x)
            return len(seen) == upper - lower + 1

        return check(k, n // 2 + 1, (1 << k) - 1) and check(k + 1, 1 << k, n)
        '''
        nums = set()
        for i in range(len(s)):
            if s[i] == "0": continue
            x = 1
            if x <= n: nums.add(x)
            for j in range(i + 1, len(s)):
                x = x * 2 + int(s[j])
                if x <= n: nums.add(x)
        
        return len(nums) == n
# @lc code=end

