#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# https://leetcode.cn/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (53.04%)
# Likes:    435
# Dislikes: 0
# Total Accepted:    120.5K
# Total Submissions: 227.2K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。
# 
# 
# 例如，"ACGAATTCCG" 是一个 DNA序列 。
# 
# 
# 在研究 DNA 时，识别 DNA 中的重复序列非常有用。
# 
# 给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序
# 返回答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 10^5
# s[i]=='A'、'C'、'G' or 'T'
# 
# 
#
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        n = len(s)
        if n <= L:
            return []
        ans = []
        x = 0
        for ch in s[:L - 1]:
            x = (x << 2) | bin[ch]
        cnt = defaultdict(int)
        for i in range(n - L + 1):
            x = ((x << 2) | bin[s[i + L - 1]]) & ((1 << (L * 2)) - 1)
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i : i + L])
        return ans
        '''
        ss = set()
        ans = set()
        n = len(s)
        for i in range(n-9):
            cur = s[i:i+10]
            if cur not in ss:
                ss.add(cur)
            else:
                ans.add(cur)
        return list(ans)
        '''
# @lc code=end

