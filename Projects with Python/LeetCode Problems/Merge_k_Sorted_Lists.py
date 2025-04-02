# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Heap:
    def __init__(self, lists):
        self.min_heap = []
        for node in lists:
            if node:  # Apenas adiciona se a lista não for vazia
                heapq.heappush(self.min_heap, HeapNode(node))

    def pop(self):
        if not self.min_heap:
            return None
        top = heapq.heappop(self.min_heap)
        next_node = top.node.next
        if next_node:
            heapq.heappush(self.min_heap, HeapNode(next_node))
        return top.node

    def push(self, novo_no):
        heapq.heappush(self.min_heap, HeapNode(novo_no))


class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        min_heap = Heap(lists)
        first = min_heap.pop()
        node = first
        while node:
            next_node = min_heap.pop()
            node.next = next_node
            node = node.next

        return first
    
lista = [None, ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
sol = Solution()
ans = sol.mergeKLists(lista)

while ans:
    print(ans.val, end=" -> ")
    ans = ans.next