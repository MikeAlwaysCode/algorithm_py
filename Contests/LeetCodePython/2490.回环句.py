#
# @lc app=leetcode.cn id=2490 lang=python3
#
# [2490] 回环句
#
# https://leetcode.cn/problems/circular-sentence/description/
#
# algorithms
# Easy (69.71%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 19.9K
# Testcase Example:  '"leetcode exercises sound delightful"'
#
# 句子 是由单个空格分隔的一组单词，且不含前导或尾随空格。
# 
# 
# 例如，"Hello World"、"HELLO"、"hello world hello world" 都是符合要求的句子。
# 
# 
# 单词 仅 由大写和小写英文字母组成。且大写和小写字母会视作不同字符。
# 
# 如果句子满足下述全部条件，则认为它是一个 回环句 ：
# 
# 
# 单词的最后一个字符和下一个单词的第一个字符相等。
# 最后一个单词的最后一个字符和第一个单词的第一个字符相等。
# 
# 
# 例如，"leetcode exercises sound delightful"、"eetcode"、"leetcode eats soul"
# 都是回环句。然而，"Leetcode is cool"、"happy Leetcode"、"Leetcode" 和 "I like Leetcode" 都
# 不 是回环句。
# 
# 给你一个字符串 sentence ，请你判断它是不是一个回环句。如果是，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：sentence = "leetcode exercises sound delightful"
# 输出：true
# 解释：句子中的单词是 ["leetcode", "exercises", "sound", "delightful"] 。
# - leetcode 的最后一个字符和 exercises 的第一个字符相等。
# - exercises 的最后一个字符和 sound 的第一个字符相等。
# - sound 的最后一个字符和 delightful 的第一个字符相等。
# - delightful 的最后一个字符和 leetcode 的第一个字符相等。
# 这个句子是回环句。
# 
# 示例 2：
# 
# 
# 输入：sentence = "eetcode"
# 输出：true
# 解释：句子中的单词是 ["eetcode"] 。
# - eetcode 的最后一个字符和 eetcode 的第一个字符相等。
# 这个句子是回环句。
# 
# 示例 3：
# 
# 
# 输入：sentence = "Leetcode is cool"
# 输出：false
# 解释：句子中的单词是 ["Leetcode", "is", "cool"] 。
# - Leetcode 的最后一个字符和 is 的第一个字符 不 相等。 
# 这个句子 不 是回环句。
# 
# 
# 
# 提示：
# 
# 
# 1 <= sentence.length <= 500
# sentence 仅由大小写英文字母和空格组成
# sentence 中的单词由单个空格进行分隔
# 不含任何前导或尾随空格
# 
# 
#

# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(len(words)):
            if words[i][0] != words[i-1][-1]:
                return False
        return True
# @lc code=end

