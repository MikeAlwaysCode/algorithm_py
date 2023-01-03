#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode.cn/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (54.33%)
# Likes:    263
# Dislikes: 0
# Total Accepted:    137.6K
# Total Submissions: 253.2K
# Testcase Example:  '"hello"'
#
# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
# 
# 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "hello"
# 输出："holle"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "leetcode"
# 输出："leotcede"
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 3 * 10^5
# s 由 可打印的 ASCII 字符组成
# 
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(ch: str) -> bool:
            return ch in "aeiouAEIOU"
        
        n = len(s)
        s = list(s)
        i, j = 0, n - 1
        while i < j:
            while i < n and not isVowel(s[i]):
                i += 1
            while j > 0 and not isVowel(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        return "".join(s)
# @lc code=end

