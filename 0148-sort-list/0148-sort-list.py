# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        if not head or not head.next:
            return head
        
        def mergeTwoLists(list1, list2):
            head = ListNode(None)
            new = head
            while list1 and list2:
                if list1.val <= list2.val:
                    new.next = list1
                    list1 = list1.next
                else:
                    new.next = list2
                    list2 = list2.next
                new = new.next

            temp = list1 if list1 else list2
            while temp:
                new.next = temp
                temp = temp.next
                new = new.next
            return head.next
        
        def middleNode(head):
            fast = slow = head
            while fast and fast.next:
                fast = fast.next.next
                temp = slow
                slow = slow.next
            temp.next = None
            return (head, slow)
        
        def solution(head):
            if not head or not head.next:
                return head
            list1, list2 = middleNode(head)
            left = solution(list1)
            right = solution(list2)
            return mergeTwoLists(left, right)
        return solution(head)