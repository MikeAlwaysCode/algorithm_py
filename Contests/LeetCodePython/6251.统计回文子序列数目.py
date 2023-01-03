#
# @lc app=leetcode.cn id=6251 lang=python3
#
# [6251] 统计回文子序列数目
#
# https://leetcode.cn/problems/count-palindromic-subsequences/description/
#
# algorithms
# Hard (40.44%)
# Likes:    10
# Dislikes: 0
# Total Accepted:    1.3K
# Total Submissions: 3.3K
# Testcase Example:  '"103301"'
#
# 给你数字字符串 s ，请你返回 s 中长度为 5 的 回文子序列 数目。由于答案可能很大，请你将答案对 10^9 + 7 取余 后返回。
# 
# 提示：
# 
# 
# 如果一个字符串从前往后和从后往前读相同，那么它是 回文字符串 。
# 子序列是一个字符串中删除若干个字符后，不改变字符顺序，剩余字符构成的字符串。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：s = "103301"
# 输出：2
# 解释：
# 总共有 6 长度为 5 的子序列："10330" ，"10331" ，"10301" ，"10301" ，"13301" ，"03301" 。
# 它们中有两个（都是 "10301"）是回文的。
# 
# 
# 示例 2：
# 
# 输入：s = "0000000"
# 输出：21
# 解释：所有 21 个长度为 5 的子序列都是 "00000" ，都是回文的。
# 
# 
# 示例 3：
# 
# 输入：s = "9999900000"
# 输出：2
# 解释：仅有的两个回文子序列是 "99999" 和 "00000" 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s 只包含数字字符。
# 
# 
#

# @lc code=start
class Solution:
    def countPalindromes(self, s: str) -> int:
        suf1 = [0] * 10
        suf2 = [0] * 100
        for d in map(int, reversed(s)):
            for j, c in enumerate(suf1):
                suf2[d * 10 + j] += c
            suf1[d] += 1
        
        ans = 0
        pre1 = [0] * 10
        pre2 = [0] * 100
        for d in map(int, s):
            suf1[d] -= 1
            for j, c in enumerate(suf1):
                suf2[d * 10 + j] -= c
            ans += sum(c1 * c2 for c1, c2 in zip(pre2, suf2))
            for j, c in enumerate(pre1):
                pre2[d * 10 + j] += c
            pre1[d] += 1
        return ans % (10 ** 9 + 7)
# @lc code=end

