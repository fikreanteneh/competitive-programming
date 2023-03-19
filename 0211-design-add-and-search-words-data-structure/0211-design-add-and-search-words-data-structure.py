class Node:
    def __init__(self):
        self.values = [None] * 26
        self.status = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        temp = self.root
        for letter in word:
            index = ord(letter) - 97
            if not temp.values[index]:
                temp.values[index] = Node()
            temp = temp.values[index]
        temp.status = True
            
    def search(self, word: str) -> bool:
        return self.searching(word, 0, self.root)
    
    def searching(self, word, index, temp):
        if not temp:
            return False
        
        if word[index] == ".":
            flag = False
            if index == len(word) - 1:
                for val in temp.values:
                    flag = flag or (val and val.status)
                return flag
            for val in temp.values:
                flag = flag or self.searching(word, index + 1, val)
            return flag
        
        
        checkIndex = ord(word[index]) - 97
        if not temp.values[checkIndex]:
            return False
        elif index == len(word) - 1:
            return temp.values[checkIndex].status
        return self.searching(word, index + 1, temp.values[checkIndex])
        
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)