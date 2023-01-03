#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#
# https://leetcode.cn/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (47.80%)
# Likes:    261
# Dislikes: 0
# Total Accepted:    18.2K
# Total Submissions: 37K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# 给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。
# 
# 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。
# 
# 
# 例如， “ace” 是 “abcde” 的子序列。
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "abcde", words = ["a","bb","acd","ace"]
# 输出: 3
# 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
# 
# 
# Example 2:
# 
# 
# 输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# 输出: 2
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= s.length <= 5 * 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# words[i]和 s 都只由小写字母组成。
# 
# ​​​​
#
import bisect
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # clist = [[] for _ in range(26)]
        clist = defaultdict(list)
        for i, c in enumerate(s):
            # clist[ord(c) - 97].append(i)
            clist[c].append(i)
        ans = 0
        for word in words:
            chk = True
            pre = -1
            for c in word:
                # j = bisect.bisect(clist[ord(c) - 97], pre)
                j = bisect.bisect(clist[c], pre)
                # if j >= len(clist[ord(c) - 97]):
                if j >= len(clist[c]):
                    chk = False
                    break
                # pre = clist[ord(c) - 97][j]
                pre = clist[c][j]
            if chk: ans += 1
        return ans
# @lc code=end

