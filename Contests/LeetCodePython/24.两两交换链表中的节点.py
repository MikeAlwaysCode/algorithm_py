#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode.cn/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (71.10%)
# Likes:    1506
# Dislikes: 0
# Total Accepted:    493.1K
# Total Submissions: 693.4K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 
# 
# 示例 2：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100
# 
# 
#
from typing import Optional


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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()

        first = head.next
        dummy.next = second = head
        
        tmp = dummy

        while first and second:
            second.next = first.next
            first.next = second
            tmp.next = first

            tmp = second
            second = second.next

            if not second:
                break
                
            first = second.next
        
        return dummy.next
# @lc code=end

