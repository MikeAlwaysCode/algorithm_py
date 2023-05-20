#
# @lc app=leetcode.cn id=1373 lang=python3
#
# [1373] 二叉搜索子树的最大键值和
#
# https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/description/
#
# algorithms
# Hard (43.11%)
# Likes:    158
# Dislikes: 0
# Total Accepted:    24.2K
# Total Submissions: 52.6K
# Testcase Example:  '[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]'
#
# 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。
# 
# 二叉搜索树的定义如下：
# 
# 
# 任意节点的左子树中的键值都 小于 此节点的键值。
# 任意节点的右子树中的键值都 大于 此节点的键值。
# 任意节点的左子树和右子树都是二叉搜索树。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# 输出：20
# 解释：键值为 3 的子树是和最大的二叉搜索树。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：root = [4,3,null,1,2]
# 输出：2
# 解释：键值为 2 的单节点子树是和最大的二叉搜索树。
# 
# 
# 示例 3：
# 
# 
# 输入：root = [-4,-2,-5]
# 输出：0
# 解释：所有节点键值都为负数，和最大的二叉搜索树为空。
# 
# 
# 示例 4：
# 
# 
# 输入：root = [2,1,3]
# 输出：6
# 
# 
# 示例 5：
# 
# 
# 输入：root = [5,4,8,3,null,6,3]
# 输出：7
# 
# 
# 
# 
# 提示：
# 
# 
# 每棵树有 1 到 40000 个节点。
# 每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。
# 
# 
#
import math
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> Tuple:
            if node is None: return (math.inf, -math.inf, 0)
            l_min, l_max, l_sum = dfs(node.left)  # 递归左子树
            r_min, r_max, r_sum = dfs(node.right)  # 递归右子树
            x = node.val
            if x <= l_max or x >= r_min:  # 不是二叉搜索树
                return (- math.inf, math.inf, 0)

            s = l_sum + r_sum + x  # 这棵子树的所有节点值之和
            nonlocal ans
            ans = max(ans, s)

            return min(l_min, x), max(r_max, x), s
        dfs(root)
        return ans
# @lc code=end

