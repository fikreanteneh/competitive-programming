# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        front = head.next
        back = head
        c = 1
        while front and front.next:
            front = front.next.next
            back = back.next
            c += 1
        temp = back
        back = back.next
        while back:
            new = back.next
            back.next = temp
            temp = back
            back = new
        maxi = 0
        while c > 0:
            if head.val != temp.val:
                return False
            head, temp = head.next, temp.next
            c -= 1
        return True
        