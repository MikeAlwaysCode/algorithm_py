#
# @lc app=leetcode.cn id=777 lang=python3
#
# [777] 在LR字符串中交换相邻字符
#
# https://leetcode.cn/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (34.38%)
# Likes:    167
# Dislikes: 0
# Total Accepted:    10.4K
# Total Submissions: 29.9K
# Testcase Example:  '"RXXLRXRXL"\n"XRLXXRRLX"'
#
# 在一个由 'L' , 'R' 和 'X'
# 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时，
# 返回True。
# 
# 
# 
# 示例 :
# 
# 输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
# 输出: True
# 解释:
# 我们可以通过以下几步将start转换成end:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= len(start) = len(end) <= 10000。
# start和end中的字符串仅限于'L', 'R'和'X'。
# 
# 
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        i = j = 0
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i < n and j < n:
                if start[i] != end[j]:
                    return False
                c = start[i]
                if c == 'L' and i < j or c == 'R' and i > j:
                    return False
                i += 1
                j += 1
        while i < n:
            if start[i] != 'X':
                return False
            i += 1
        while j < n:
            if end[j] != 'X':
                return False
            j += 1
        return True
# @lc code=end

