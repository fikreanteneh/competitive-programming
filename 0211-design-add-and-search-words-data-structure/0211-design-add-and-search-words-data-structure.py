class Node:
    def __init__(self):
        self.values = defaultdict(list)
        self.status = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        temp = self.root
        for letter in word:
            if not temp.values[letter]:
                temp.values[letter] = Node()
            temp = temp.values[letter]
        temp.status = True
            
    def search(self, word: str) -> bool:
        return self.searching(word, 0, self.root)
    
    def searching(self, word, index, temp):
        if not temp:
            return False
        
        if word[index] == ".":
            flag = False
            if index == len(word) - 1:
                for val, nodes in temp.values.items():
                    flag = flag or (nodes and nodes.status)
                return flag
            for val, nodes in temp.values.items():
                flag = flag or self.searching(word, index + 1, nodes)
            return flag
        
        if not temp.values[word[index]]:
            return False
        elif index == len(word) - 1:
            return temp.values[word[index]].status
        return self.searching(word, index + 1, temp.values[word[index]])
        
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)