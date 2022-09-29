# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        if len(lists) <=1 : return lists[0]
        if len(lists)%2 != 0: 
            lists.append(None)
        new = []
        for i in range(1, len(lists), 2):
            new.append(self.merge(lists[i-1], lists[i]))
        return self.mergeKLists(new)
    
    def merge(self, list1, list2):
            head = ListNode()
            tail = head
            while list1 and list2:
                if list1.val <= list2.val:
                    new = ListNode(list1.val)
                    tail.next = new
                    list1 = list1.next
                else:
                    new = ListNode(list2.val)
                    tail.next = new
                    list2 = list2.next
                tail = tail.next
            if list1: tail.next = list1
            if list2: tail.next = list2
            return head.next
        
