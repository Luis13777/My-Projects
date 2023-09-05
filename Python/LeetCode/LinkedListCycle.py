# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        visited = set()
        p = head
        while (p):
            if (p in visited):
                return True
            visited.add(p)
            p = p.next
        
        return False
    
MyList = ListNode(3)

MyList.next = ListNode(2)

MyList.next.next = ListNode(0)
MyList.next.next.next = ListNode(-4)
# MyList.next.next.next.next = MyList.next

print(Solution().hasCycle(MyList))
