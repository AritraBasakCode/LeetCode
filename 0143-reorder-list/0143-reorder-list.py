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
        if not head:
            return
        
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        curr = head
        for _ in range(len(stack)//2):
            last = stack.pop()
            nxt = curr.next
            curr.next = last
            last.next = nxt

            curr = nxt
        curr.next = None