#
# @lc app=leetcode.cn id=2564 lang=python3
#
# [2564] 子字符串异或查询
#
# https://leetcode.cn/problems/substring-xor-queries/description/
#
# algorithms
# Medium (36.33%)
# Likes:    19
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 13K
# Testcase Example:  '"101101"\n[[0,5],[1,2]]'
#
# 给你一个 二进制字符串 s 和一个整数数组 queries ，其中 queries[i] = [firsti, secondi] 。
# 
# 对于第 i 个查询，找到 s 的 最短子字符串 ，它对应的 十进制值 val 与 firsti 按位异或 得到 secondi ，换言之，val ^
# firsti == secondi 。
# 
# 第 i 个查询的答案是子字符串 [lefti, righti] 的两个端点（下标从 0 开始），如果不存在这样的子字符串，则答案为 [-1, -1]
# 。如果有多个答案，请你选择 lefti 最小的一个。
# 
# 请你返回一个数组 ans ，其中 ans[i] = [lefti, righti] 是第 i 个查询的答案。
# 
# 子字符串 是一个字符串中一段连续非空的字符序列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "101101", queries = [[0,5],[1,2]]
# 输出：[[0,2],[2,3]]
# 解释：第一个查询，端点为 [0,2] 的子字符串为 "101" ，对应十进制数字 5 ，且 5 ^ 0 = 5 ，所以第一个查询的答案为
# [0,2]。第二个查询中，端点为 [2,3] 的子字符串为 "11" ，对应十进制数字 3 ，且 3 ^ 1 = 2 。所以第二个查询的答案为 [2,3]
# 。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "0101", queries = [[12,8]]
# 输出：[[-1,-1]]
# 解释：这个例子中，没有符合查询的答案，所以返回 [-1,-1] 。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "1", queries = [[4,5]]
# 输出：[[0,0]]
# 解释：这个例子中，端点为 [0,0] 的子字符串对应的十进制值为 1 ，且 1 ^ 4 = 5 。所以答案为 [0,0] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s[i] 要么是 '0' ，要么是 '1' 。
# 1 <= queries.length <= 10^5
# 0 <= firsti, secondi <= 10^9
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n, m = len(s), {}
        if (i := s.find('0')) >= 0:
            m[0] = (i, i)  # 这样下面就可以直接跳过 '0' 了，效率更高
        for l, c in enumerate(s):
            if c == '0': continue
            x = 0
            for r in range(l, min(l + 30, n)):
                x = (x << 1) | (ord(s[r]) & 1)
                if x not in m:
                    m[x] = (l, r)
        NOT_FOUND = (-1, -1)
        return [m.get(x ^ y, NOT_FOUND) for x, y in queries]
        '''
        n = len(s)
        ans = []
        d = dict()
        for fir, sec in queries:
            xor = bin(fir ^ sec)[2:]
            if len(xor) > n:
                ans.append([-1, -1])
                continue
            if xor in d:
                l = d[xor]
            else:
                l = s.find(xor)
                d[xor] = l
            if l == -1:
                ans.append([-1, -1])
                continue
            ans.append([l, l + len(xor) - 1])
        return ans
        '''
# @lc code=end

