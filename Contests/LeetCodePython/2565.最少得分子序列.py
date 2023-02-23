#
# @lc app=leetcode.cn id=2565 lang=python3
#
# [2565] 最少得分子序列
#
# https://leetcode.cn/problems/subsequence-with-the-minimum-score/description/
#
# algorithms
# Hard (35.04%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 6.6K
# Testcase Example:  '"abacaba"\n"bzaa"'
#
# 给你两个字符串 s 和 t 。
# 
# 你可以从字符串 t 中删除任意数目的字符。
# 
# 如果没有从字符串 t 中删除字符，那么得分为 0 ，否则：
# 
# 
# 令 left 为删除字符中的最小下标。
# 令 right 为删除字符中的最大下标。
# 
# 
# 字符串的得分为 right - left + 1 。
# 
# 请你返回使 t 成为 s 子序列的最小得分。
# 
# 一个字符串的 子序列 是从原字符串中删除一些字符后（也可以一个也不删除），剩余字符不改变顺序得到的字符串。（比方说 "ace" 是 "abcde"
# 的子序列，但是 "aec" 不是）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "abacaba", t = "bzaa"
# 输出：1
# 解释：这个例子中，我们删除下标 1 处的字符 "z" （下标从 0 开始）。
# 字符串 t 变为 "baa" ，它是字符串 "abacaba" 的子序列，得分为 1 - 1 + 1 = 1 。
# 1 是能得到的最小得分。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cde", t = "xyz"
# 输出：3
# 解释：这个例子中，我们将下标为 0， 1 和 2 处的字符 "x" ，"y" 和 "z" 删除（下标从 0 开始）。
# 字符串变成 "" ，它是字符串 "cde" 的子序列，得分为 2 - 0 + 1 = 3 。
# 3 是能得到的最小得分。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length, t.length <= 10^5
# s 和 t 都只包含小写英文字母。
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        suf = [m] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and s[i] == t[j]:
                j -= 1
            suf[i] = j + 1
        ans = suf[0]  # 删除 t[:suf[0]]
        if ans == 0: return 0

        j = 0
        for i, c in enumerate(s):
            if c == t[j]:  # 注意 j 不会等于 m，因为上面 suf[0]>0 表示 t 不是 s 的子序列
                j += 1
                ans = min(ans, suf[i + 1] - j)  # 删除 t[j:suf[i+1]]
        return ans
        '''
        n, m = len(s), len(t)
        
        pos = [[] for _ in range(26)]
        for i, c in enumerate(s):
            pos[ord(c) - 97].append(i)
        
        pre = []
        fr = -1
        for i, c in enumerate(t):
            idx = ord(c) - 97
            if not pos[idx] or fr > pos[idx][-1]:
                break
            j = bisect.bisect_left(pos[idx], fr)
            fr = pos[idx][j]
            pre.append((fr, i))
            fr += 1
        
        if not pre:
            ans = m
        else:
            ans = m - pre[-1][1] - 1
        
        if ans == 0: return ans
        # print(pre)
        fr = n
        for i in range(m - 1, -1, -1):
            idx = ord(t[i]) - 97
            if not pos[idx] or fr < pos[idx][0]:
                break
            j = bisect.bisect(pos[idx], fr)
            fr = pos[idx][j - 1] - 1
            while pre and pre[-1][0] > fr:
                pre.pop()
            l = -1 if not pre else pre[-1][1]
            # print(l, i, fr, i - l - 1)
            ans = min(ans, max(0, i - l - 1))

        return ans
        '''
# @lc code=end

