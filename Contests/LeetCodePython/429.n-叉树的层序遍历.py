#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#
# https://leetcode.cn/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (72.54%)
# Likes:    334
# Dislikes: 0
# Total Accepted:    138.6K
# Total Submissions: 191.1K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
# 
# 树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[[1],[3,2,4],[5,6]]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# 输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
# 
# 
# 
# 
# 提示：
# 
# 
# 树的高度不会超过 1000
# 树的节点总数在 [0, 10^4] 之间
# 
# 
#
from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = [root]
        while q:
            tmp = q
            q = []
            curr = []
            for x in tmp:
                curr.append(x.val)
                for c in x.children:
                    q.append(c)
            ans.append(curr)
        return ans
# @lc code=end

