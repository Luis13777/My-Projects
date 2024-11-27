class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if (not head):
            return
        
        p = head
        data = []
        while (p):
            data.append(p.val)
            p=p.next

        data = data[::-1]
        reversedList = ListNode ()
        p = reversedList
        for i in range (len(data)):
            p.val = data[i]
            if (i != len(data) - 1):
                p.next = ListNode ()
            p = p.next


        return reversedList
    

# O(n)