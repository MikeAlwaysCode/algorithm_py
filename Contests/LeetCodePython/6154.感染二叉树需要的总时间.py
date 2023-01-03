#
# @lc app=leetcode.cn id=6154 lang=python3
#
# [6154] 感染二叉树需要的总时间
#
# https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/description/
#
# algorithms
# Medium (41.67%)
# Likes:    7
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 9.6K
# Testcase Example:  '[1,5,3,null,4,10,6,9,2]\n3'
#
# 给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start
# 的节点开始爆发。
# 
# 每分钟，如果节点满足以下全部条件，就会被感染：
# 
# 
# 节点此前还没有感染。
# 节点与一个已感染节点相邻。
# 
# 
# 返回感染整棵树需要的分钟数。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [1,5,3,null,4,10,6,9,2], start = 3
# 输出：4
# 解释：节点按以下过程被感染：
# - 第 0 分钟：节点 3
# - 第 1 分钟：节点 1、10、6
# - 第 2 分钟：节点5
# - 第 3 分钟：节点 4
# - 第 4 分钟：节点 9 和 2
# 感染整棵树需要 4 分钟，所以返回 4 。
# 
# 
# 示例 2：
# 
# 输入：root = [1], start = 1
# 输出：0
# 解释：第 0 分钟，树中唯一一个节点处于感染状态，返回 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [1, 10^5] 内
# 1 <= Node.val <= 10^5
# 每个节点的值 互不相同
# 树中必定存在值为 start 的节点
# 
# 
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = {}
        def dfs(node, p):
            if node is None:
                return
            if node.val == start:
                self.start = node
            parents[node] = p
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)

        ans = -1
        visit = {self.start, None}
        q = [self.start]
        while q:
            ans += 1
            tmp = q
            q = []
            for node in tmp:
                for x in node.left, node.right, parents[node]:
                    if x not in visit:
                        visit.add(x)
                        q.append(x)
        
        return ans
# @lc code=end

