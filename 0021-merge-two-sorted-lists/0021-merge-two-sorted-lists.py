class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None)
        new = head
        self.solution(new, list1, list2)
        return head.next
    
    
    def solution(self, head, list1, list2):
        if not list1 or not list2:
            temp = list1 if not list2 else list2
            
            while temp:
                head.next = temp
                temp = temp.next
                head = head.next 
            return
        
        if list1.val <= list2.val:
            head.next = list1
            list1 = list1.next
            
        else:
            head.next = list2
            list2 = list2.next
            
        head = head.next
        self.solution(head, list1, list2)
            
