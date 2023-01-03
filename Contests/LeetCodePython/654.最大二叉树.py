#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#
# https://leetcode.cn/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (81.53%)
# Likes:    523
# Dislikes: 0
# Total Accepted:    137.8K
# Total Submissions: 166.7K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:
# 
# 
# 创建一个根节点，其值为 nums 中的最大值。
# 递归地在最大值 左边 的 子数组前缀上 构建左子树。
# 递归地在最大值 右边 的 子数组后缀上 构建右子树。
# 
# 
# 返回 nums 构建的 最大二叉树 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,2,1,6,0,5]
# 输出：[6,3,5,null,2,0,null,null,1]
# 解释：递归调用如下所示：
# - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
# ⁠   - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
# ⁠       - 空数组，无子节点。
# ⁠       - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
# ⁠           - 空数组，无子节点。
# ⁠           - 只有一个元素，所以子节点是一个值为 1 的节点。
# ⁠   - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
# ⁠       - 只有一个元素，所以子节点是一个值为 0 的节点。
# ⁠       - 空数组，无子节点。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,1]
# 输出：[3,null,2,null,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# nums 中的所有整数 互不相同
# 
# 
#
from typing import List, Optional
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        stk = list()
        tree = [None] * n

        for i in range(n):
            tree[i] = TreeNode(nums[i])
            while stk and nums[i] > nums[stk[-1]]:
                tree[i].left = tree[stk[-1]]
                stk.pop()
            if stk:
                tree[stk[-1]].right = tree[i]
            stk.append(i)
        
        return tree[stk[0]]
        '''
        def construct(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            best = left
            for i in range(left + 1, right + 1):
                if nums[i] > nums[best]:
                    best = i
        
            node = TreeNode(nums[best])
            node.left = construct(left, best - 1)
            node.right = construct(best + 1, right)
            return node
        
        return construct(0, len(nums) - 1)
        '''
# @lc code=end

