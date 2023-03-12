#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode.cn/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (73.40%)
# Likes:    1416
# Dislikes: 0
# Total Accepted:    269.8K
# Total Submissions: 367.7K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 
# 回文串 是正着读和反着读都一样的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a"
# 输出：[["a"]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由小写英文字母组成
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)
        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())
                return

            for j in range(i, n):
                t = s[i:j + 1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()
        
        dfs(0)
        return ans
# @lc code=end

