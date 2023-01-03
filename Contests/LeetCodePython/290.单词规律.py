#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# https://leetcode.cn/problems/word-pattern/description/
#
# algorithms
# Easy (44.90%)
# Likes:    514
# Dislikes: 0
# Total Accepted:    118K
# Total Submissions: 262.9K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
# 
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。
# 
# 
# 
# 示例1:
# 
# 
# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true
# 
# 示例 2:
# 
# 
# 输入:pattern = "abba", s = "dog cat cat fish"
# 输出: false
# 
# 示例 3:
# 
# 
# 输入: pattern = "aaaa", s = "dog cat cat dog"
# 输出: false
# 
# 
# 
# 提示:
# 
# 
# 1 <= pattern.length <= 300
# pattern 只包含小写英文字母
# 1 <= s.length <= 3000
# s 只包含小写英文字母和 ' '
# s 不包含 任何前导或尾随对空格
# s 中每个单词都被 单个空格 分隔
# 
# 
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        d1 = dict()
        d2 = dict()

        for c, word in zip(pattern, words):
            if c not in d1 and word not in d2:
                d1[c] = word
                d2[word] = c
            elif c not in d1 or word not in d2:
                return False
            elif word != d1[c] or c != d2[word]:
                return False
        
        return True
# @lc code=end

