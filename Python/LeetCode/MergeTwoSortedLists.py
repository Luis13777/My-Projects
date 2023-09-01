class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None and list2 == None:
            return
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        p = head

        while list1 or list2:
            if list1 != None and list2 != None:
                if list1.val <= list2.val:
                    p.next = list1
                    list1 = list1.next
                else:
                    p.next = list2
                    list2 = list2.next
                p = p.next
            elif list1 == None:
                p.next = list2
                list2 = None
            elif list2 == None:
                p.next = list1
                list1 = None

        return head
    
MyList1 = ListNode(1)
MyList1.next = ListNode(2)
MyList1.next.next = ListNode(4)

MyList2 = ListNode(1)
MyList2.next = ListNode(3)
MyList2.next.next = ListNode(4)

MergedList = Solution().mergeTwoLists(MyList1, MyList2)

while MergedList:
    print(MergedList.val)
    MergedList = MergedList.next