# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 1. 哈希集
# public class Solution {
#     public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
#         Set<ListNode> visited = new HashSet<ListNode>();
#         ListNode temp = headA;
#         while (temp != null) {
#             visited.add(temp);
#             temp = temp.next;
#         }
#         temp = headB;
#         while (temp != null) {
#             if (visited.contains(temp)) {
#                 return temp;
#             }
#             temp = temp.next;
#         }
#         return null;
#     }
# }
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         s = set()
#         tmp = headA
#         while tmp:
#             s.add(tmp)
#             tmp = tmp.next
#         tmp = headB
#         while tmp:
#             if tmp in s:
#                 return tmp
#             tmp = tmp.next
#         return None
# 2. 双指针
# public class Solution {
#     public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
#         if (headA == null || headB == null) {
#             return null;
#         }
#         ListNode pA = headA, pB = headB;
#         while (pA != pB) {
#             pA = pA == null ? headB : pA.next;
#             pB = pB == null ? headA : pB.next;
#         }
#         return pA;
#     }
# }
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        currA, currB = headA, headB
        while currA != currB:
            currA = headB if not currA else currA.next
            currB = headA if not currB else currB.next
            
        return currA
