#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#
# https://leetcode.cn/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (47.59%)
# Likes:    842
# Dislikes: 0
# Total Accepted:    150.8K
# Total Submissions: 317K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# 
# 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true
# ；否则，返回 false 。
# 
# 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,4,5,1,2], subRoot = [4,1,2]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# root 树上的节点数量范围是 [1, 2000]
# subRoot 树上的节点数量范围是 [1, 1000]
# -10^4 
# -10^4 
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def getMaxElement(node: Optional[TreeNode]) -> None:
            nonlocal maxElement
            if node is None:
                return
            
            maxElement = max(maxElement, node.val)
            getMaxElement(node.left)
            getMaxElement(node.right)

        def getDfsOrder(node: Optional[TreeNode], order: list[int]) -> None:
            if node is None:
                return

            order.append(node.val)
            if node.left:
                getDfsOrder(node.left, order)
            else:
                order.append(lNull)
            
            if node.right:
                getDfsOrder(node.right, order)
            else:
                order.append(rNull)

        def kmp() -> bool:
            rLen, sLen = len(rOrder), len(sOrder)

            fail = [-1] * sLen
            for i in range(1, sLen):
                j = fail[i - 1]
                while j != -1 and sOrder[j + 1] != sOrder[i]:
                    j = fail[j]
                if sOrder[j + 1] == sOrder[i]:
                    j += 1
                fail[i] = j
            
            j = -1
            for i in range(rLen):
                while j != -1 and sOrder[j + 1] != rOrder[i]:
                    j = fail[j]
                if sOrder[j + 1] == rOrder[i]:
                    j += 1
                    if j == sLen - 1:
                        return True

            return False

        maxElement = - math.inf
        getMaxElement(root)
        getMaxElement(subRoot)
        
        lNull = maxElement + 1
        rNull = maxElement + 2

        rOrder, sOrder = [], []
        getDfsOrder(root, rOrder)
        getDfsOrder(subRoot, sOrder)

        return kmp()
# @lc code=end

