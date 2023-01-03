#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode.cn/problems/reorder-list/description/
#
# algorithms
# Medium (64.44%)
# Likes:    1071
# Dislikes: 0
# Total Accepted:    220K
# Total Submissions: 341.4K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
# 
# 
# L0 → L1 → … → Ln - 1 → Ln
# 
# 
# 请将其重新排列后变为：
# 
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
# 
# 示例 2：
# 
# 
# 
# 
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
        # 
# 
# 
# 提示：
# 
# 
# 链表的长度范围为 [1, 5 * 10^4]
# 1 <= node.val <= 1000
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def getMid(node: Optional[ListNode]) -> Optional[ListNode]:
            first = second = node
            while first.next and first.next.next:
                first = first.next.next
                second = second.next
            return second
        
        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            pre = None
            cur = node
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
            
        l1 = head
        mid = getMid(head)
        l2 = reverse(mid.next)
        mid.next = None

        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next
            # if tmp1 == l2:
            #     tmp1 = None
            # if  tmp1 == l2.next:
            #     tmp2 = None
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2
# @lc code=end

