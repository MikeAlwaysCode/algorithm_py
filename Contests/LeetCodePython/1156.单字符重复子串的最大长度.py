#
# @lc app=leetcode.cn id=1156 lang=python3
#
# [1156] 单字符重复子串的最大长度
#
# https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/description/
#
# algorithms
# Medium (48.58%)
# Likes:    154
# Dislikes: 0
# Total Accepted:    14.3K
# Total Submissions: 29.5K
# Testcase Example:  '"ababa"'
#
# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
# 
# 给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
# 
# 
# 
# 示例 1：
# 
# 输入：text = "ababa"
# 输出：3
# 
# 
# 示例 2：
# 
# 输入：text = "aaabaaa"
# 输出：6
# 
# 
# 示例 3：
# 
# 输入：text = "aaabbaaa"
# 输出：4
# 
# 
# 示例 4：
# 
# 输入：text = "aaaaa"
# 输出：5
# 
# 
# 示例 5：
# 
# 输入：text = "abcdef"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= text.length <= 20000
# text 仅由小写英文字母组成。
# 
# 
#
from collections import Counter


# @lc code=start
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        ans, n = 0, len(text)
        cnt = Counter(text)
        dp = [[0] * 2 for _ in range(n + 1)]
        for i, c in enumerate(text):
            if i and c == text[i - 1]:
                dp[i + 1][0] = dp[i][0] + 1
                dp[i + 1][1] = dp[i][1] + 1
            else:
                dp[i + 1][0] = 1
                dp[i + 1][1] = 2
                if i > 1 and c == text[i - 2]:
                    dp[i + 1][1] += dp[i - 1][0]
            ans = max(ans, dp[i + 1][0])
            ans = max(ans, dp[i + 1][1] if cnt[c] >= dp[i + 1][1] else dp[i + 1][1] - 1)
        return ans
# @lc code=end

