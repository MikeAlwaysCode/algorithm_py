#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode.cn/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (70.82%)
# Likes:    2041
# Dislikes: 0
# Total Accepted:    322.3K
# Total Submissions: 454.9K
# Testcase Example:  '3'
#
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：5
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
# f = [0] * 20
# f[0] = f[1] = 1
# for i in range(2, 20):
#     k = (i - 1) // 2
#     if k * 2 == i - 1:
#         f[i] = f[k] * f[k]
#     k += 1
#     for j in range(k, i):
#         f[i] += f[j] * f[i - j - 1] * 2

class Solution:
    def numTrees(self, n: int) -> int:
        # return f[n]
        C = 1
        for i in range(0, n):
            C = C * 2 * (2 * i + 1) // (i + 2)
        return C
# @lc code=end

def main():
    sol = Solution()

    n = 5
    print(sol.numTrees(n))

if __name__ == '__main__':
    main()

