#
# @lc app=leetcode.cn id=1358 lang=python3
#
# [1358] 包含所有三种字符的子字符串数目
#
# https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/description/
#
# algorithms
# Medium (52.86%)
# Likes:    93
# Dislikes: 0
# Total Accepted:    11.1K
# Total Submissions: 20.9K
# Testcase Example:  '"abcabc"'
#
# 给你一个字符串 s ，它只包含三种字符 a, b 和 c 。
# 
# 请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "abcabc"
# 输出：10
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab",
# "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
# 
# 
# 示例 2：
# 
# 输入：s = "aaacb"
# 输出：3
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
# 
# 
# 示例 3：
# 
# 输入：s = "abc"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= s.length <= 5 x 10^4
# s 只包含字符 a，b 和 c 。
# 
# 
#
from collections import Counter

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        cnt = Counter()
        l = 0
        for r, c in enumerate(s):
            cnt[c] += 1
            while len(cnt) == 3 and all(v for v in cnt.values()):
                cnt[s[l]] -= 1
                l += 1
            if len(cnt) == 3: ans += l
        return ans
# @lc code=end

