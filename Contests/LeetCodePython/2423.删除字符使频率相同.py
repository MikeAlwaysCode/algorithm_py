#
# @lc app=leetcode.cn id=2423 lang=python3
#
# [2423] 删除字符使频率相同
#
# https://leetcode.cn/problems/remove-letter-to-equalize-frequency/description/
#
# algorithms
# Easy (19.23%)
# Likes:    52
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 49.2K
# Testcase Example:  '"abcc"'
#
# 给你一个下标从 0 开始的字符串 word ，字符串只包含小写英文字母。你需要选择 一个 下标并 删除 下标处的字符，使得 word 中剩余每个字母出现
# 频率 相同。
# 
# 如果删除一个字母后，word 中剩余所有字母的出现频率都相同，那么返回 true ，否则返回 false 。
# 
# 注意：
# 
# 
# 字母 x 的 频率 是这个字母在字符串中出现的次数。
# 你 必须 恰好删除一个字母，不能一个字母都不删除。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：word = "abcc"
# 输出：true
# 解释：选择下标 3 并删除该字母，word 变成 "abc" 且每个字母出现频率都为 1 。
# 
# 
# 示例 2：
# 
# 输入：word = "aazz"
# 输出：false
# 解释：我们必须删除一个字母，所以要么 "a" 的频率变为 1 且 "z" 的频率为 2
# ，要么两个字母频率反过来。所以不可能让剩余所有字母出现频率相同。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= word.length <= 100
# word 只包含小写英文字母。
# 
# 
#

# @lc code=start
class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = list(sorted(Counter(word).values()))
        return len(cnt) == 1 or (cnt[0] == 1 and cnt[1] == cnt[-1]) or (cnt[-1] == cnt[-2] + 1 and cnt[-2] == cnt[0])
# @lc code=end

