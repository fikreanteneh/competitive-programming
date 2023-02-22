class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
        while list1:
            new.next = list1
            list1 = list1.next
            new = new.next
        while list2:
            new.next = list2
            list2 = list2.next
            new = new.next
        return head.next
#             head = ListNode()
#             tail = head
#             while list1 and list2:
#                 if list1.val <= list2.val:
#                     new = ListNode(list1.val)
#                     tail.next = new
#                     list1 = list1.next
#                 else:
#                     new = ListNode(list2.val)
#                     tail.next = new
#                     list2 = list2.next
#                 tail = tail.next
                
#             if list1: tail.next = list1
#             if list2: tail.next = list2
#             return head.next