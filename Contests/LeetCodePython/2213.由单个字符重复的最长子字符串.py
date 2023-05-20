#
# @lc app=leetcode.cn id=2213 lang=python3
#
# [2213] 由单个字符重复的最长子字符串
#
# https://leetcode.cn/problems/longest-substring-of-one-repeating-character/description/
#
# algorithms
# Hard (39.26%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 7.5K
# Testcase Example:  '"babacc"\n"bcb"\n[1,3,3]'
#
# 给你一个下标从 0 开始的字符串 s 。另给你一个下标从 0 开始、长度为 k 的字符串 queryCharacters ，一个下标从 0 开始、长度也是
# k 的整数 下标 数组 queryIndices ，这两个都用来描述 k 个查询。
# 
# 第 i 个查询会将 s 中位于下标 queryIndices[i] 的字符更新为 queryCharacters[i] 。
# 
# 返回一个长度为 k 的数组 lengths ，其中 lengths[i] 是在执行第 i 个查询 之后 s 中仅由 单个字符重复 组成的 最长子字符串 的
# 长度 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
# 输出：[3,3,4]
# 解释：
# - 第 1 次查询更新后 s = "bbbacc" 。由单个字符重复组成的最长子字符串是 "bbb" ，长度为 3 。
# - 第 2 次查询更新后 s = "bbbccc" 。由单个字符重复组成的最长子字符串是 "bbb" 或 "ccc"，长度为 3 。
# - 第 3 次查询更新后 s = "bbbbcc" 。由单个字符重复组成的最长子字符串是 "bbbb" ，长度为 4 。
# 因此，返回 [3,3,4] 。
# 
# 示例 2：
# 
# 
# 输入：s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
# 输出：[2,3]
# 解释：
# - 第 1 次查询更新后 s = "abazz" 。由单个字符重复组成的最长子字符串是 "zz" ，长度为 2 。
# - 第 2 次查询更新后 s = "aaazz" 。由单个字符重复组成的最长子字符串是 "aaa" ，长度为 3 。
# 因此，返回 [2,3] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s 由小写英文字母组成
# k == queryCharacters.length == queryIndices.length
# 1 <= k <= 10^5
# queryCharacters 由小写英文字母组成
# 0 <= queryIndices[i] < s.length
# 
# 
#
from typing import List


# @lc code=start
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        s = list(s)
        n = len(s)
        pre = [0] * (4 * n)
        suf = [0] * (4 * n)
        mx = [0] * (4 * n)

        def maintain(o: int, l: int, r: int) -> None:
            pre[o] = pre[o * 2]
            suf[o] = suf[o * 2 + 1]
            mx[o] = max(mx[o * 2], mx[o * 2 + 1])
            m = (l + r) // 2
            if s[m - 1] == s[m]:  # 中间字符相同，可以合并
                if suf[o * 2] == m - l + 1:
                    pre[o] += pre[o * 2 + 1]
                if pre[o * 2 + 1] == r - m:
                    suf[o] += suf[o * 2]
                mx[o] = max(mx[o], suf[o * 2] + pre[o * 2 + 1])

        def build(o: int, l: int, r: int) -> None:
            if l == r:
                pre[o] = suf[o] = mx[o] = 1
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            maintain(o, l, r)

        def update(o: int, l: int, r: int, i: int) -> None:
            if l == r: return
            m = (l + r) // 2
            if i <= m:
                update(o * 2, l, m, i)
            else:
                update(o * 2 + 1, m + 1, r, i)
            maintain(o, l, r)

        build(1, 1, n)
        ans = []
        for c, i in zip(queryCharacters, queryIndices):
            s[i] = c
            update(1, 1, n, i + 1)
            ans.append(mx[1])
        return ans
# @lc code=end

