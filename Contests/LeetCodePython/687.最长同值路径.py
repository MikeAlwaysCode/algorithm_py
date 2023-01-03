#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#
# https://leetcode.cn/problems/longest-univalue-path/description/
#
# algorithms
# Medium (45.38%)
# Likes:    629
# Dislikes: 0
# Total Accepted:    54.5K
# Total Submissions: 118.5K
# Testcase Example:  '[5,4,5,1,1,null,5]'
#
# 给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。
# 
# 两个节点之间的路径长度 由它们之间的边数表示。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入：root = [5,4,5,1,1,5]
# 输出：2
# 
# 
# 示例 2:
# 
# 
# 
# 
# 输入：root = [1,4,5,4,4,5]
# 输出：2
# 
# 
# 
# 
# 提示:
# 
# 
# 树的节点数的范围是 [0, 10^4] 
# -1000 <= Node.val <= 1000
# 树的深度将不超过 1000 
# 
# 
#
from typing import Optional
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            left2 = left + 1 if node.left and node.left.val == node.val else 0
            
            right2 = right + 1 if node.right and node.right.val == node.val else 0
            
            nonlocal ans
            ans = max(ans, left2 + right2)
            return max(left2, right2)
        
        dfs(root)
        return ans
# @lc code=end

