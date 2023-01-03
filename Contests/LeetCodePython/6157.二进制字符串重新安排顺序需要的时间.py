#
# @lc app=leetcode.cn id=6157 lang=python3
#
# [6157] 二进制字符串重新安排顺序需要的时间
#
# https://leetcode.cn/problems/time-needed-to-rearrange-a-binary-string/description/
#
# algorithms
# Medium (54.70%)
# Likes:    7
# Dislikes: 0
# Total Accepted:    3.6K
# Total Submissions: 6.6K
# Testcase Example:  '"0110101"'
#
# 给你一个二进制字符串 s 。在一秒之中，所有 子字符串 "01" 同时 被替换成 "10" 。这个过程持续进行到没有 "01" 存在。
# 
# 请你返回完成这个过程所需要的秒数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "0110101"
# 输出：4
# 解释：
# 一秒后，s 变成 "1011010" 。
# 再过 1 秒后，s 变成 "1101100" 。
# 第三秒过后，s 变成 "1110100" 。
# 第四秒后，s 变成 "1111000" 。
# 此时没有 "01" 存在，整个过程花费 4 秒。
# 所以我们返回 4 。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "11100"
# 输出：0
# 解释：
# s 中没有 "01" 存在，整个过程花费 0 秒。
# 所以我们返回 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s[i] 要么是 '0' ，要么是 '1' 。
# 
# 
#

# @lc code=start
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        f = pre0 = 0

        for c in s:
            if c == '0':
                pre0 += 1
            elif pre0:
                f = max(f + 1, pre0)
        return f
        '''
        n = len(s)
        v = []
        for i in range(n):
            if s[i] == '0':
                v.append(i)
        if not v:
            return 0
        n0 = len(v)
        ans = 0
        while v[0] < n - n0:
            for i in range(n0):
                if v[i] < n - n0 + i and ( i == n0 - 1 or v[i] < v[i+1] - 1 ):
                    v[i] += 1
            ans += 1
        return ans
        '''
# @lc code=end

