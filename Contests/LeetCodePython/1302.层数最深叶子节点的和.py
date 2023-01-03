#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
#
# https://leetcode.cn/problems/deepest-leaves-sum/description/
#
# algorithms
# Medium (84.51%)
# Likes:    104
# Dislikes: 0
# Total Accepted:    32.3K
# Total Submissions: 38.3K
# Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
#
# 给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# 输出：15
# 
# 
# 示例 2：
# 
# 
# 输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：19
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 10^4] 之间。
# 1 
# 
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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([root])
        while q:
            ans = 0
            for _ in range(len(q)):
                node = q.popleft()
                ans += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
        '''
        ans = 0
        q = list()
        q.append(root)
        while q:
            tmp = list()
            ans = 0
            for curr in q:
                ans += curr.val
                if curr.left:
                    tmp.append(curr.left)
                if curr.right:
                    tmp.append(curr.right)
            q = tmp
        return ans
        '''
        '''
        maxLevel, ans = -1, 0
        def dfs(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return
            nonlocal maxLevel, ans
            if level > maxLevel:
                maxLevel, ans = level, node.val
            elif level == maxLevel:
                ans += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return ans
        '''
# @lc code=end

