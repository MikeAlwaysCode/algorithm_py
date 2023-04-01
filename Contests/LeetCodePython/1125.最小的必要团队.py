#
# @lc app=leetcode.cn id=1125 lang=python3
#
# [1125] 最小的必要团队
#
# https://leetcode.cn/problems/smallest-sufficient-team/description/
#
# algorithms
# Hard (50.78%)
# Likes:    93
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 9.6K
# Testcase Example:  '["java","nodejs","reactjs"]\n[["java"],["nodejs"],["nodejs","reactjs"]]'
#
# 作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」（ 编号为 i
# 的备选人员 people[i] 含有一份该备选人员掌握的技能列表）。
# 
# 所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills
# 中列出的每项技能，团队中至少有一名成员已经掌握。可以用每个人的编号来表示团队中的成员：
# 
# 
# 例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 people[3] 的备选人员。
# 
# 
# 请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按 任意顺序 返回答案，题目数据保证答案存在。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：req_skills = ["java","nodejs","reactjs"], people =
# [["java"],["nodejs"],["nodejs","reactjs"]]
# 输出：[0,2]
# 
# 
# 示例 2：
# 
# 
# 输入：req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people
# =
# [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# req_skills[i] 由小写英文字母组成
# req_skills 中的所有字符串 互不相同
# 1 
# 0 
# 1 
# people[i][j] 由小写英文字母组成
# people[i] 中的所有字符串 互不相同
# people[i] 中的每个技能是 req_skills 中的技能
# 题目数据保证「必要团队」一定存在
# 
# 
#
from functools import cache
import math
from typing import List


# @lc code=start
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(req_skills), len(people)
        skill_id = {skill:i for i, skill in enumerate(req_skills)}

        dp = [math.inf] * (1 << n)
        dp[0] = 0
        ans = [[] for _ in range(1 << n)]

        for i in range(m):
            ps = 0
            for skill in people[i]:
                ps |= 1 << skill_id[skill]
            
            for mask in range(1 << n):
                if dp[mask] == math.inf: continue
                nmask = mask | ps
                if dp[mask] + 1 < dp[nmask]:
                    dp[nmask] = dp[mask] + 1
                    ans[nmask] = ans[mask] + [i]
        
        return ans[(1 << n) - 1]
        '''
        ps = [0] * m
        can = [[] for _ in range(n)]
        for i in range(m):
            for skill in people[i]:
                ps[i] |= 1 << skill_id[skill]
                can[skill_id[skill]].append(i)
        
        @cache
        def dfs(state):
            if state == (1 << n) - 1:
                return []
            cnt = math.inf
            res = []
            for i in range(n):
                if not (state >> i) & 1:
                    for j in can[i]:
                        cur = [j] + dfs(state|ps[j])
                        if len(cur) < cnt:
                            cnt = len(cur)
                            res = cur
            return res
        
        return dfs(0)
        '''
# @lc code=end

