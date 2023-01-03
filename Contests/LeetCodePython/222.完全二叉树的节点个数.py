#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
# https://leetcode.cn/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (80.52%)
# Likes:    830
# Dislikes: 0
# Total Accepted:    241.5K
# Total Submissions: 299.9K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
# 
# 完全二叉树
# 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h
# 层，则该层包含 1~ 2^h 个节点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,4,5,6]
# 输出：6
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目范围是[0, 5 * 10^4]
# 0 
# 题目数据保证输入的树是 完全二叉树
# 
# 
# 
# 
# 进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        level = 0
        node = root
        while node.left:
            level += 1
            node = node.left

        def exist(root, l, k) -> bool:
            node = root
            bits = 1 << (l - 1)
            while node and bits:
                if bits & k:
                    node = node.right
                else:
                    node = node.left
                
                bits >>= 1
            return node is not None

        low, high = 1 << level, (1 << (level + 1)) - 1
        while low < high:
            mid = low + high + 1 >> 1
            if exist(root, level, mid):
                low = mid
            else:
                high = mid - 1
        return low
# @lc code=end

