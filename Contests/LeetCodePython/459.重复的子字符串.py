#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#
# https://leetcode.cn/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (51.06%)
# Likes:    835
# Dislikes: 0
# Total Accepted:    155.7K
# Total Submissions: 304.9K
# Testcase Example:  '"abab"'
#
# 给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "abab"
# 输出: true
# 解释: 可由子串 "ab" 重复两次构成。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "aba"
# 输出: false
# 
# 
# 示例 3:
# 
# 
# 输入: s = "abcabcabcabc"
# 输出: true
# 解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 
# 1 <= s.length <= 10^4
# s 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(pattern: str) -> bool:
            n = len(pattern)
            fail = [-1] * n
            for i in range(1, n):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1
            return fail[n - 1] != -1 and n % (n - fail[n - 1] - 1) == 0
        
        return kmp(s)
        # return (s + s).find(s, 1) != len(s)
        # n = len(s)
        # for i in range(1, n // 2 + 1):
        #     if n % i == 0:
        #         if all(s[j] == s[j - i] for j in range(i, n)):
        #             return True
        # return False
# @lc code=end

