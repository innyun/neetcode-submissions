class Node:
    def __init__(self):
        self.children = {}
        self.end = False
    

class PrefixTree:

    def __init__(self):
        self.t = Node()

    def insert(self, word: str) -> None:
        temp = self.t
        for i, l in enumerate(word):
            if l in temp.children:
                temp = temp.children[l]
            else:
                temp.children[l] = Node()
                temp = temp.children[l]
            if i == len(word) - 1:
                temp.end = True

    def search(self, word: str) -> bool:
        temp = self.t
        for i, l in enumerate(word):
            if l not in temp.children:
                return False
            else:
                temp = temp.children[l]
            if i == len(word) - 1 and temp.end:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        temp = self.t
        for l in prefix:
            if l not in temp.children:
                return False
            temp = temp.children[l]
        return True