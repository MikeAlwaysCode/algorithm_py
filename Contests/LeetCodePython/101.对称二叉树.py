#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode.cn/problems/symmetric-tree/description/
#
# algorithms
# Easy (58.32%)
# Likes:    2156
# Dislikes: 0
# Total Accepted:    711.5K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
# 
#
from collections import deque
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # BFS
        q = deque([root.left, root.right])
        while q:
            node1 = q.popleft()
            node2 = q.popleft()
            if node1 is None and node2 is None:
                continue
            elif (node1 is None or node2 is None) or (node1.val != node2.val):
                return False
            
            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)
        return True

        # # DFS
        # def check(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        #     if left is None and right is None:
        #         return True
        #     elif left is None or right is None:
        #         return False
            
        #     if left.val != right.val:
        #         return False
            
        #     return check(left.left, right.right) and check(left.right, right.left)

        # return check(root.left, root.right)
# @lc code=end

