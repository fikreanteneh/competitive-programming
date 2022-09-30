# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        if length == 0: return None
        if length <=1 : return lists[0]
        new = []
        for i in range(0, length, 2):
            l1 = lists[i]
            if i+1 >= length: l2 = None
            else: l2 = lists[i+1]
            new.append(self.merge(l1,l2))
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
