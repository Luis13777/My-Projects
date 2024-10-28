# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head) -> None:
        listOfPointers = []
        a = head
        while a != None:
            listOfPointers.append(a)
            a = a.next

        r = len(listOfPointers) - 1
        l = 0



        while (l <= r):
            if (r-l > 1):
                listOfPointers[l].next = listOfPointers[r]
                listOfPointers[r].next = listOfPointers[l+1]
            elif (r-l == 1):
                listOfPointers[l].next = listOfPointers[r]
                listOfPointers[r].next = None
            elif (r - l == 0):
                listOfPointers[l].next = None
            l += 1
            r -= 1


        a = head
        while (a):
            print(a.val)
            a = a.next

        pass

MyList = ListNode(1)
MyList.next = ListNode (2)
MyList.next.next = ListNode (3)
MyList.next.next.next = ListNode (4)
MyList.next.next.next.next = ListNode (5)

solution = Solution()
solution.reorderList(MyList)