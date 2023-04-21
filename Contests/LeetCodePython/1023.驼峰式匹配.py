#
# @lc app=leetcode.cn id=1023 lang=python3
#
# [1023] 驼峰式匹配
#
# https://leetcode.cn/problems/camelcase-matching/description/
#
# algorithms
# Medium (57.54%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    13.8K
# Total Submissions: 22.7K
# Testcase Example:  '["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]\n"FB"'
#
# 如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0
# 个字符。）
# 
# 给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串
# pattern 匹配时， answer[i] 才为 true，否则为 false。
# 
# 
# 
# 示例 1：
# 
# 输入：queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FB"
# 输出：[true,false,true,true,false]
# 示例：
# "FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
# "FootBall" 可以这样生成："F" + "oot" + "B" + "all".
# "FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".
# 
# 示例 2：
# 
# 输入：queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FoBa"
# 输出：[true,false,true,false,false]
# 解释：
# "FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
# "FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".
# 
# 
# 示例 3：
# 
# 输出：queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FoBaT"
# 输入：[false,true,false,false,false]
# 解释： 
# "FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= queries.length <= 100
# 1 <= queries[i].length <= 100
# 1 <= pattern.length <= 100
# 所有字符串都仅由大写和小写英文字母组成。
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = [True] * len(queries)
        for i, s in enumerate(queries):
            j = 0
            for c in s:
                if j < len(pattern) and c == pattern[j]:
                    j += 1
                elif c.isupper():
                    ans[i] = False
                    break
            if ans[i] and j < len(pattern):
                ans[i] = False
        return ans
# @lc code=end

