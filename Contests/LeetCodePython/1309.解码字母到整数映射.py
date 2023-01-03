#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#
# https://leetcode.cn/problems/decrypt-string-from-alphabet-to-integer-mapping/description/
#
# algorithms
# Easy (76.70%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    25K
# Total Submissions: 32.6K
# Testcase Example:  '"10#11#12"'
#
# 给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：
# 
# 
# 字符（'a' - 'i'）分别用（'1' - '9'）表示。
# 字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
# 
# 
# 返回映射之后形成的新字符串。
# 
# 题目数据保证映射始终唯一。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "10#11#12"
# 输出："jkab"
# 解释："j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
# 
# 
# 示例 2：
# 
# 
# 输入：s = "1326#"
# 输出："acz"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s[i] 只包含数字（'0'-'9'）和 '#' 字符。
# s 是映射始终存在的有效字符串。
# 
# 
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                ans.append(chr(int(s[i-2:i]) + 96))
                i -= 3
            else:
                ans.append(chr(int(s[i]) + 96))
                i -= 1
        return "".join(ans[::-1])
# @lc code=end

