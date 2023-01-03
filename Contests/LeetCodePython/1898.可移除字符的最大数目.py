#
# @lc app=leetcode.cn id=1898 lang=python3
#
# [1898] 可移除字符的最大数目
#
# https://leetcode.cn/problems/maximum-number-of-removable-characters/description/
#
# algorithms
# Medium (36.45%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    7.5K
# Total Submissions: 20.7K
# Testcase Example:  '"abcacb"\n"ab"\n[3,1,0]'
#
# 给你两个字符串 s 和 p ，其中 p 是 s 的一个 子序列 。同时，给你一个元素 互不相同 且下标 从 0 开始 计数的整数数组 removable
# ，该数组是 s 中下标的一个子集（s 的下标也 从 0 开始 计数）。
# 
# 请你找出一个整数 k（0 ），选出 removable 中的 前 k 个下标，然后从 s 中移除这些下标对应的 k 个字符。整数 k
# 需满足：在执行完上述步骤后， p 仍然是 s 的一个 子序列 。更正式的解释是，对于每个 0  ，先标记出位于 s[removable[i]]
# 的字符，接着移除所有标记过的字符，然后检查 p 是否仍然是 s 的一个子序列。
# 
# 返回你可以找出的 最大 k ，满足在移除字符后 p 仍然是 s 的一个子序列。
# 
# 字符串的一个 子序列 是一个由原字符串生成的新字符串，生成过程中可能会移除原字符串中的一些字符（也可能不移除）但不改变剩余字符之间的相对顺序。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "abcacb", p = "ab", removable = [3,1,0]
# 输出：2
# 解释：在移除下标 3 和 1 对应的字符后，"abcacb" 变成 "accb" 。
# "ab" 是 "accb" 的一个子序列。
# 如果移除下标 3、1 和 0 对应的字符后，"abcacb" 变成 "ccb" ，那么 "ab" 就不再是 s 的一个子序列。
# 因此，最大的 k 是 2 。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
# 输出：1
# 解释：在移除下标 3 对应的字符后，"abcbddddd" 变成 "abcddddd" 。
# "abcd" 是 "abcddddd" 的一个子序列。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "abcab", p = "abc", removable = [0,1,2,3,4]
# 输出：0
# 解释：如果移除数组 removable 的第一个下标，"abc" 就不再是 s 的一个子序列。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 0 
# p 是 s 的一个 子字符串
# s 和 p 都由小写英文字母组成
# removable 中的元素 互不相同
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        ns, np = len(s), len(p)
        n = len(removable)
        # 辅助函数，用来判断移除 k 个下标后 p 是否是 s_k 的子序列
        def check(k: int) -> bool:
            state = [True] * ns   # s 中每个字符的状态
            for i in range(k):
                state[removable[i]] = False
            # 匹配 s_k 与 p 
            j = 0
            for i in range(ns):
                # s[i] 未被删除且与 p[j] 相等时，匹配成功，增加 j
                if state[i] and s[i] == p[j]:
                    j += 1
                    if j == np:
                        return True
            return False
        
        # 二分查找
        l, r = 0, n + 1
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1
# @lc code=end

