# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        numero1 = ''
        numero2 = ''

        percorredor = l1
        while(percorredor is not None):
            numero1 += str(percorredor.val)
            percorredor = percorredor.next

        percorredor = l2
        while(percorredor is not None):
            numero2 += str(percorredor.val)
            percorredor = percorredor.next

        numero1 = numero1[::-1]
        numero2 = numero2[::-1]


        numero = int(numero1) + int(numero2)
        numero = str(numero)
        numero = numero[::-1]
        

        tamanho = len(str(numero))
        i = 0
        Lista = ListNode()
        aux = Lista
        aux.val = str(numero)[0]
        i = 1
        while (i<tamanho):
            proximo = ListNode(str(numero)[i])
            aux.next = proximo
            aux = aux.next
            i += 1
            proximo = None
        aux = None

        return(Lista)



sol = Solution()

alg1 = ListNode(1)
alg1.next = ListNode(2)
alg1.next.next = ListNode(3)

alg2 = ListNode(4)
alg2.next = ListNode(5)
alg2.next.next = ListNode(6)

Lista = sol.addTwoNumbers(alg1,alg2)
aux = Lista
while (aux is not None):
    print (aux.val)
    aux = aux.next