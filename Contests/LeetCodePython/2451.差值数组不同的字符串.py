#
# @lc app=leetcode.cn id=2451 lang=python3
#
# [2451] 差值数组不同的字符串
#
# https://leetcode.cn/problems/odd-string-difference/description/
#
# algorithms
# Easy (57.05%)
# Likes:    1
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 5.7K
# Testcase Example:  '["adc","wzy","abc"]'
#
# 给你一个字符串数组 words ，每一个字符串长度都相同，令所有字符串的长度都为 n 。
# 
# 每个字符串 words[i] 可以被转化为一个长度为 n - 1 的 差值整数数组 difference[i] ，其中对于 0 <= j <= n - 2
# 有 difference[i][j] = words[i][j+1] - words[i][j] 。注意两个字母的差值定义为它们在字母表中 位置
# 之差，也就是说 'a' 的位置是 0 ，'b' 的位置是 1 ，'z' 的位置是 25 。
# 
# 
# 比方说，字符串 "acb" 的差值整数数组是 [2 - 0, 1 - 2] = [2, -1] 。
# 
# 
# words 中所有字符串 除了一个字符串以外 ，其他字符串的差值整数数组都相同。你需要找到那个不同的字符串。
# 
# 请你返回 words中 差值整数数组 不同的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：words = ["adc","wzy","abc"]
# 输出："abc"
# 解释：
# - "adc" 的差值整数数组是 [3 - 0, 2 - 3] = [3, -1] 。
# - "wzy" 的差值整数数组是 [25 - 22, 24 - 25]= [3, -1] 。
# - "abc" 的差值整数数组是 [1 - 0, 2 - 1] = [1, 1] 。
# 不同的数组是 [1, 1]，所以返回对应的字符串，"abc"。
# 
# 
# 示例 2：
# 
# 
# 输入：words = ["aaa","bob","ccc","ddd"]
# 输出："bob"
# 解释：除了 "bob" 的差值整数数组是 [13, -13] 以外，其他字符串的差值整数数组都是 [0, 0] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= words.length <= 100
# n == words[i].length
# 2 <= n <= 20
# words[i] 只含有小写英文字母。
# 
# 
#
import collections
from typing import List


# @lc code=start
class Solution:
    def oddString(self, words: List[str]) -> str:
        '''
        d = defaultdict(list)
        for s in words:
            d[tuple(ord(x) - ord(y) for x, y in pairwise(s))].append(s)
        x, y = d.values()
        return x[0] if len(x) == 1 else y[0]
        '''
        cnt = collections.defaultdict(int)
        d = dict()

        for word in words:
            diff = ord(word[0]) - 97
            conv = ""
            for i, c in enumerate(word):
                conv += chr(ord(c) - diff)
            cnt[conv] += 1
            d[conv] = word
        
        for k, v in cnt.items():
            if v == 1:
                return d[k]
# @lc code=end

