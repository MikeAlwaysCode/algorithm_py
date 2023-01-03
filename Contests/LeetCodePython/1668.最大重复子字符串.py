#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#
# https://leetcode.cn/problems/maximum-repeating-substring/description/
#
# algorithms
# Easy (44.43%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    16.8K
# Total Submissions: 36.2K
# Testcase Example:  '"ababc"\n"ab"'
#
# 给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的
# 重复值为 k 。单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence
# 的子串，那么重复值 k 为 0 。
# 
# 给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：sequence = "ababc", word = "ab"
# 输出：2
# 解释："abab" 是 "ababc" 的子字符串。
# 
# 
# 示例 2：
# 
# 
# 输入：sequence = "ababc", word = "ba"
# 输出：1
# 解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
# 
# 
# 示例 3：
# 
# 
# 输入：sequence = "ababc", word = "ac"
# 输出：0
# 解释："ac" 不是 "ababc" 的子字符串。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# sequence 和 word 都只包含小写英文字母。
# 
# 
#

# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        if n < m:
            return 0

        fail = [-1] * m
        for i in range(1, m):
            j = fail[i - 1]
            while j != -1 and word[j + 1] != word[i]:
                j = fail[j]
            if word[j + 1] == word[i]:
                fail[i] = j + 1
        
        f = [0] * n
        j = -1
        for i in range(n):
            while j != -1 and word[j + 1] != sequence[i]:
                j = fail[j]
            if word[j + 1] == sequence[i]:
                j += 1
                if j == m - 1:
                    f[i] = (0 if i == m - 1 else f[i - m]) + 1
                    j = fail[j]
        
        return max(f)
        '''
        n, m = len(sequence), len(word)
        if n < m:
            return 0
        
        f = [0] * n
        for i in range(m - 1, n):
            valid = True
            for j in range(m):
                if sequence[i - m + j + 1] != word[j]:
                    valid = False
                    break
            if valid:
                f[i] = (0 if i == m - 1 else f[i - m]) + 1
        
        return max(f)
        '''
# @lc code=end

