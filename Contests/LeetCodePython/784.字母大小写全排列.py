#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#
# https://leetcode.cn/problems/letter-case-permutation/description/
#
# algorithms
# Medium (70.34%)
# Likes:    417
# Dislikes: 0
# Total Accepted:    73.5K
# Total Submissions: 104.6K
# Testcase Example:  '"a1b2"'
#
# 给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。
# 
# 返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# 
# 示例 2:
# 
# 
# 输入: s = "3z4"
# 输出: ["3z4","3Z4"]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= s.length <= 12
# s 由小写英文字母、大写英文字母和数字组成
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        
        bits = sum(c.isalpha() for c in s)

        for bit in range(1<<bits):
            b = 0
            word = []
            for c in s:
                if c.isalpha():
                    if ( bit >> b) & 1:
                        word.append(c.upper())
                    else:
                        word.append(c.lower())
                    b += 1
                else:
                    word.append(c)

            ans.append("".join(word))
        return ans
# @lc code=end

