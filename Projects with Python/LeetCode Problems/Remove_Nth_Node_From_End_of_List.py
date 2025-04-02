# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        p_before = head
        p_last = head

        for _ in range(n):
            p_last = p_last.next

        if p_last is None:
            return head.next
        
        while (p_last.next):
            p_last = p_last.next
            p_before = p_before.next

        p_before.next = p_before.next.next

        return head
    

# Example usage:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)

resposta = Solution().removeNthFromEnd(head, 2)

while resposta:
    print(resposta.val)
    resposta = resposta.next

    

        