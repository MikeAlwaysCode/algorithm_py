#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#
# https://leetcode.cn/problems/next-greater-node-in-linked-list/description/
#
# algorithms
# Medium (60.98%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    47.1K
# Total Submissions: 73.8K
# Testcase Example:  '[2,1,5]'
#
# 给定一个长度为 n 的链表 head
# 
# 对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。
# 
# 返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。如果第 i
# 个节点没有下一个更大的节点，设置 answer[i] = 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：head = [2,1,5]
# 输出：[5,5,0]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：head = [2,7,4,3,5]
# 输出：[7,0,5,5,0]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数为 n
# 1 <= n <= 10^4
# 1 <= Node.val <= 10^9
# 
# 
#
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stk = []
        idx = -1
        while head:
            idx += 1
            ans.append(0)
            while stk and stk[-1][0] < head.val:
                ans[stk.pop()[1]] = head.val
            stk.append((head.val, idx))
            head = head.next
        return ans
# @lc code=end

