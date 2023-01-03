#
# @lc app=leetcode.cn id=6247 lang=python3
#
# [6247] 从链表中移除节点
#
# https://leetcode.cn/problems/remove-nodes-from-linked-list/description/
#
# algorithms
# Medium (67.59%)
# Likes:    7
# Dislikes: 0
# Total Accepted:    4.6K
# Total Submissions: 6.8K
# Testcase Example:  '[5,2,13,3,8]'
#
# 给你一个链表的头节点 head 。
# 
# 对于列表中的每个节点 node ，如果其右侧存在一个具有 严格更大 值的节点，则移除 node 。
# 
# 返回修改后链表的头节点 head 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：head = [5,2,13,3,8]
# 输出：[13,8]
# 解释：需要移除的节点是 5 ，2 和 3 。
# - 节点 13 在节点 5 右侧。
# - 节点 13 在节点 2 右侧。
# - 节点 8 在节点 3 右侧。
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,1,1,1]
# 输出：[1,1,1,1]
# 解释：每个节点的值都是 1 ，所以没有需要移除的节点。
# 
# 
# 
# 
# 提示：
# 
# 
# 给定列表中的节点数目在范围 [1, 10^5] 内
# 1 <= Node.val <= 10^5
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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        nxt = self.removeNodes(head.next)
        if nxt is None or nxt.val <= head.val:
            head.next = nxt
            return head
            
        return nxt
        '''
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        n = len(nums)
        suff = [0] * n
        mx = 0
        for i in range(n - 1, -1, -1):
            suff[i] = mx
            mx = max(mx, nums[i])
        i = 0
        dummy = ListNode(0, head)
        cur = head
        pre = dummy
        while cur:
            if cur.val < suff[i]:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
            i += 1
        return dummy.next
        '''
# @lc code=end

