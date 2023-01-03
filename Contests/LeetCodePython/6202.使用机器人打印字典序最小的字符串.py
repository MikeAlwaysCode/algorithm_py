#
# @lc app=leetcode.cn id=6202 lang=python3
#
# [6202] 使用机器人打印字典序最小的字符串
#
# https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description/
#
# algorithms
# Medium (31.93%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 8.3K
# Testcase Example:  '"zza"'
#
# 给你一个字符串 s 和一个机器人，机器人当前有一个空字符串 t 。执行以下操作之一，直到 s 和 t 都变成空字符串：
# 
# 
# 删除字符串 s 的 第一个 字符，并将该字符给机器人。机器人把这个字符添加到 t 的尾部。
# 删除字符串 t 的 最后一个 字符，并将该字符给机器人。机器人将该字符写到纸上。
# 
# 
# 请你返回纸上能写出的字典序最小的字符串。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "zza"
# 输出："azz"
# 解释：用 p 表示写出来的字符串。
# 一开始，p="" ，s="zza" ，t="" 。
# 执行第一个操作三次，得到 p="" ，s="" ，t="zza" 。
# 执行第二个操作三次，得到 p="azz" ，s="" ，t="" 。
# 
# 
# 示例 2：
# 
# 输入：s = "bac"
# 输出："abc"
# 解释：用 p 表示写出来的字符串。
# 执行第一个操作两次，得到 p="" ，s="c" ，t="ba" 。
# 执行第二个操作两次，得到 p="ab" ，s="c" ，t="" 。
# 执行第一个操作，得到 p="ab" ，s="" ，t="c" 。
# 执行第二个操作，得到 p="abc" ，s="" ，t="" 。
# 
# 
# 示例 3：
# 
# 输入：s = "bdda"
# 输出："addb"
# 解释：用 p 表示写出来的字符串。
# 一开始，p="" ，s="bdda" ，t="" 。
# 执行第一个操作四次，得到 p="" ，s="" ，t="bdda" 。
# 执行第二个操作四次，得到 p="addb" ，s="" ，t="" 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s 只包含小写英文字母。
# 
# 
#

# @lc code=start
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        stk = []
        # ans = [""] * n
        ans = []

        suf = [0] * n
        suf[-1] = ord(s[-1]) - 97
        for i in range(n-2, -1, -1):
            suf[i] = min(suf[i+1], ord(s[i]) - 97)

        # j = 0
        for i, c in enumerate(s):
            while stk and (ord(stk[-1]) - 97) <= suf[i]:
                v = stk.pop()
                ans.append(v)
                # ans[j] = v
                # j += 1
                
            if (ord(c) - 97) == suf[i]:
                ans.append(c)
                # ans[j] = c
                # j += 1
            else:
                stk.append(c)
            
        return "".join(ans) + "".join(stk[::-1])
# @lc code=end

