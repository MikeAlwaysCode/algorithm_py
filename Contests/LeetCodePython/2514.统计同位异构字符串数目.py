#
# @lc app=leetcode.cn id=2514 lang=python3
#
# [2514] 统计同位异构字符串数目
#
# https://leetcode.cn/problems/count-anagrams/description/
#
# algorithms
# Hard (46.23%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 5K
# Testcase Example:  '"too hot"'
#
# 给你一个字符串 s ，它包含一个或者多个单词。单词之间用单个空格 ' ' 隔开。
# 
# 如果字符串 t 中第 i 个单词是 s 中第 i 个单词的一个 排列 ，那么我们称字符串 t 是字符串 s 的同位异构字符串。
# 
# 
# 比方说，"acb dfe" 是 "abc def" 的同位异构字符串，但是 "def cab" 和 "adc bef" 不是。
# 
# 
# 请你返回 s 的同位异构字符串的数目，由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "too hot"
# 输出：18
# 解释：输入字符串的一些同位异构字符串为 "too hot" ，"oot hot" ，"oto toh" ，"too toh" 以及 "too oht"
# 。
# 
# 
# 示例 2：
# 
# 输入：s = "aa"
# 输出：1
# 解释：输入字符串只有一个同位异构字符串。
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s 只包含小写英文字母和空格 ' ' 。
# 相邻单词之间由单个空格隔开。
# 
# 
#

# @lc code=start
class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        ans = 1
        n = len(s)
        # 阶乘
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i % MOD
        # 逆元
        inverse = [0] * (n + 1)
        inverse[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inverse[i-1] = inverse[i] * i % MOD

        words = s.split()
        for word in words:
            cnt = Counter(word)
            res = fact[len(word)]
            for v in cnt.values():
                res = res * inverse[v] % MOD
            ans = ans * res % MOD
        return ans
# @lc code=end

