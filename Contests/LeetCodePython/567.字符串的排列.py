#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode.cn/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.24%)
# Likes:    778
# Dislikes: 0
# Total Accepted:    227K
# Total Submissions: 513.2K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
# 
# 换句话说，s1 的排列之一是 s2 的 子串 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
# 
# 
# 示例 2：
# 
# 
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 和 s2 仅包含小写字母
# 
# 
#
from collections import Counter, defaultdict
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        d = defaultdict(int)
        n = len(s1)
        left = 0
        diff = len(cnt)
        for right, c in enumerate(s2):
            d[c] += 1
            if d[c] == cnt[c]:
                diff -= 1
            elif d[c] == cnt[c] + 1:
                diff += 1

            if right - left + 1 > n:
                d[s2[left]] -= 1
                if d[s2[left]] == cnt[s2[left]] - 1:
                    diff += 1
                elif d[s2[left]] == cnt[s2[left]]:
                    diff -= 1
                left += 1

            if right - left + 1 == n and not diff:
                return True
            
        return False
# @lc code=end

