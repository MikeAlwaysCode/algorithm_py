#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode.cn/problems/word-break/description/
#
# algorithms
# Medium (53.82%)
# Likes:    1855
# Dislikes: 0
# Total Accepted:    378.3K
# Total Submissions: 702.9K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
# 
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 
# 
# 示例 2：
# 
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
# 注意，你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅有小写英文字母组成
# wordDict 中的所有字符串 互不相同
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ss = set(wordDict)
        n = len(s)
        f = [False] * (n + 10)
        f[0] = True
        for i in range(1, n + 1):
            j = i
            while j >= 1 and not f[i]:
                sub = s[j - 1:i]
                if sub in ss:
                    f[i] = f[j - 1]
                j -= 1
        return f[n]
# @lc code=end

