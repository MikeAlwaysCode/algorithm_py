#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (54.84%)
# Likes:    1038
# Dislikes: 0
# Total Accepted:    240.2K
# Total Submissions: 438.1K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= s.length, p.length <= 3 * 10^4
# s 和 p 仅包含小写字母
# 
# 
#
import collections
from typing import Counter, List


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        chk = collections.defaultdict(int)
        n = len(p)
        diff = len(set(p))
        ans = []
        for i, c in enumerate(s):
            chk[c] += 1
            if chk[c] == cnt[c]:
                diff -= 1
            elif chk[c] == cnt[c] + 1:
                diff += 1

            if i >= n:
                d = s[i-n]
                chk[d] -= 1
                if chk[d] == cnt[d]:
                    diff -= 1
                elif chk[d] == cnt[d] - 1:
                    diff += 1
            if not diff:
                ans.append(i-n+1)
        return ans
# @lc code=end

