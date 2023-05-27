#
# @lc app=leetcode.cn id=1080 lang=python3
#
# [1080] 根到叶路径上的不足节点
#
# https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/description/
#
# algorithms
# Medium (52.54%)
# Likes:    115
# Dislikes: 0
# Total Accepted:    11.6K
# Total Submissions: 20.4K
# Testcase Example:  '[1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]\n1'
#
# 给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。
# 
# 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。
# 
# 叶子节点，就是没有子节点的节点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
# 输出：[1,2,3,4,null,null,7,8,9,null,14]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
# 输出：[5,4,8,11,null,17,4,7,null,null,null,5]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1,2,-3,-5,null,4,null], limit = -1
# 输出：[1,null,-3,4]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 5000] 内
# -10^5 <= Node.val <= 10^5
# -10^9 <= limit <= 10^9
# 
# 
# 
# 
#
import math
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
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        limit -= root.val
        if root.left is root.right:  # root 是叶子
            # 如果 limit > 0 说明从根到叶子的路径和小于 limit，删除叶子，否则不删除
            return None if limit > 0 else root
        if root.left: root.left = self.sufficientSubset(root.left, limit)
        if root.right: root.right = self.sufficientSubset(root.right, limit)
        # 如果有儿子没被删除，就不删 root，否则删 root
        return root if root.left or root.right else None
# @lc code=end

