class Node:
    def __init__(self):
        self.child = [None]*26
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()
        
    def wordToListNumber(self, value):
        if type(value) != str:
            return value
        val = []
        for char in value:
            val.append(ord(char)-97)
        return val

    def insert(self, value) -> None:
        new = self.root
        value = self.wordToListNumber(value)
        for index in value:
            if new.child[index] is None:
                new.child[index] = Node()
            new = new.child[index]
        new.end = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.tree = Trie()
        for word in words:
            self.tree.insert(word[::-1])
        self.letter = []

    def query(self, letter: str) -> bool:
        self.letter.append(ord(letter)-97)
        return self.search()
    
    def search(self):
        head = self.tree.root
        for val in reversed(self.letter):
            head = head.child[val]
            if not head: break
            if head.end: return True
        return False
            
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)