#
# @lc app=leetcode.cn id=6166 lang=python3
#
# [6166] 最大回文数字
#
# https://leetcode.cn/problems/largest-palindromic-number/description/
#
# algorithms
# Medium (27.62%)
# Likes:    3
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 19.4K
# Testcase Example:  '"444947137"'
#
# 给你一个仅由数字（0 - 9）组成的字符串 num 。
# 
# 请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。
# 
# 注意：
# 
# 
# 你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。
# 数字可以重新排序。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num = "444947137"
# 输出："7449447"
# 解释：
# 从 "444947137" 中选用数字 "4449477"，可以形成回文整数 "7449447" 。
# 可以证明 "7449447" 是能够形成的最大回文整数。
# 
# 
# 示例 2：
# 
# 
# 输入：num = "00009"
# 输出："9"
# 解释：
# 可以证明 "9" 能够形成的最大回文整数。
# 注意返回的整数不应含前导零。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= num.length <= 10^5
# num 由数字（0 - 9）组成
# 
# 
#
from collections import Counter
# @lc code=start
class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = Counter(num)
        v = list(cnt.items())
        v.sort(reverse=True)

        head = []
        tail = []
        preNum = False
        maxOne = -1
        zero = False
        for d, c in v:
            if c > 1:
                if d != '0' or preNum:
                    k = c // 2
                    ds = d * k
                    head.append(ds)
                    tail.append(ds)
                    if d != '0':
                        preNum = True
            if c&1:
                maxOne = max(maxOne, int(d))
            if d == '0':
                zero = True
            # print(d, c)
        # print(head)
        # print(tail)
        # print(maxOne)
        if maxOne != -1:
            mid = str(maxOne)
        elif not preNum and zero:
            mid = "0"
        else:
            mid = ""
        return "".join(head) + mid + "".join(tail[::-1])
# @lc code=end

