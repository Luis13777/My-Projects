from collections import deque

class Node:
    def __init__(self, letra, posicao):
        self.letra = letra
        self.posicao = posicao
        self.parent = None
        # Filho a esquerda
        self.right_sibling = None
        # Irmao a direita
        self.left_child = None

class Tree:
    def __init__(self):
        self.root = None

    def find_node(self, node, posicao):
        if node is None:
            return None
        if node.posicao == posicao:
            return node
        search = self.find_node(node.right_sibling, posicao)
        if search is not None:
            return search
        return self.find_node(node.left_child, posicao)
    

    def insert(self, letra, posicao, parent_posicao):
        new_node = Node(letra, posicao)
        parent_node = self.find_node(self.root, parent_posicao)
        new_node.parent = parent_node

        if parent_node.left_child is None:
            parent_node.left_child = new_node
        else:
            sibling_node = parent_node.left_child
            while sibling_node.right_sibling is not None:
                sibling_node = sibling_node.right_sibling
            sibling_node.right_sibling = new_node
    
    def traverse_node(self, node):
        print(node.letra)
        if node.left_child is not None:
            self.traverse_node(node.left_child)
        if node.right_sibling is not None:
            self.traverse_node(node.right_sibling)

    def breadth_first_traversal(self):
        resposta = ''
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            resposta += node.letra
            if node.left_child is not None:
                node = node.left_child
                while node is not None:
                    queue.append(node)
                    node = node.right_sibling
        return resposta
    
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows != 1):
        # montar arvore
            arvore = Tree()
            arvore.root = Node("", 0)
            voltar = False
            j = 0
            i = 0
            while (i<len(s)):  
                arvore.insert(s[i], i + 1, j)
                if (j==0):
                    j = i
                i += 1
                if (numRows - j%(numRows*2-2) == 1):
                    voltar = True
                if voltar:
                    j -= 1
                    if (j%(numRows*2-2) == 0):
                        j = 0
                        voltar = False
                else:
                    j += 1

            return arvore.breadth_first_traversal()
        else:
            return s

solucao = Solution()
print(solucao.convert("A", 1))