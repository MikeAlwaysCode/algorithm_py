#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Medium (41.80%)
# Likes:    1667
# Dislikes: 0
# Total Accepted:    773.7K
# Total Submissions: 1.8M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0
# 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
# 
# 
# 示例 2：
# 
# 
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= haystack.length, needle.length <= 10^4
# haystack 和 needle 仅由小写英文字符组成
# 
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        
        # KMP Algorithm
        # txt: original , pat: pattern
        def KMPpreprocess(pat):
            i, length, n = 1, 0, len(pat)
            lps = [0] * n
            while i < n:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
            return lps

        def KMPsearch(txt, pat):
            m, n = len(txt), len(pat)
            if not n:
                return 0
            lps = KMPpreprocess(pat)
            i = j = 0
            while i < m:
                if txt[i] == pat[j]:
                    i += 1
                    j += 1
                if j == n:
                    return i - j
                if i < m and txt[i] != pat[j]:
                    if j:
                        j = lps[j - 1]
                    else:
                        i += 1
            return -1

        return KMPsearch(haystack, needle)
# @lc code=end

