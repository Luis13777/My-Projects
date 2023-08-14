class Node:
    def __init__(self, char):
        self.char = char
        self.childrens = []
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:

        p = self.root

        j = 0
        while (j < len(word)):

            # checking if c is already inserted
            Inserted = False
            i = 0
            while (not Inserted and i < len(p.childrens)):
                if p.childrens[i].char == word[j]:
                    Inserted = True
                    i -= 1
                i += 1



            if Inserted:
                p = p.childrens[i]
                j += 1
            else:
                for c in word[j::]:
                    p.childrens.append(Node(c))
                    p = p.childrens[-1]
                j = len(word)

            if (j == len(word)):
                p.end = True
    

    def search(self, word: str) -> bool:
        p = self.root

        j = 0
        while (j < len(word)):

            # checking if c is already inserted
            Inserted = False
            i = 0
            while (not Inserted and i < len(p.childrens)):
                if p.childrens[i].char == word[j]:
                    Inserted = True
                    i -= 1
                i += 1

            if Inserted:
                p = p.childrens[i]
                j += 1
            else:
                return False

            if  p.end == True and j == len(word):
                return True
        return False
    
    def startsWith(self, prefix: str) -> bool:
        p = self.root

        j = 0
        while (j < len(prefix)):

            # checking if c is already inserted
            Inserted = False
            i = 0
            while (not Inserted and i < len(p.childrens)):
                if p.childrens[i].char == prefix[j]:
                    Inserted = True
                    i -= 1
                i += 1

            if Inserted:
                p = p.childrens[i]
                j += 1
            else:
                return False


        return True

obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))


