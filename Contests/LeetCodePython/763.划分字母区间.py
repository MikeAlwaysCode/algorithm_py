#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
# https://leetcode.cn/problems/partition-labels/description/
#
# algorithms
# Medium (76.85%)
# Likes:    846
# Dislikes: 0
# Total Accepted:    140.1K
# Total Submissions: 182.3K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
# 
# 
# 
# 示例：
# 
# 
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
# 
# 
# 
# 
# 提示：
# 
# 
# S的长度在[1, 500]之间。
# S只包含小写字母 'a' 到 'z' 。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i
        
        partition = list()
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        
        return partition
# @lc code=end

