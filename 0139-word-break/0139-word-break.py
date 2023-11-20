class Node:
    def __init__(self):
        self.end = False
        self.children = [None]*26
class Trie:
    def __init__(self):
        self.root = Node()
    def add(self, word):
        curr = self.root
        for letter in word:
            index = ord(letter) - ord("a")
            if not curr.children[index]:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.end = True
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        indexes = [-1]
        n = len(s)
        for i in range(n):
            for j in range(len(indexes) - 1, -1, -1):
                if s[indexes[j] + 1:i+1] in wordDict:
                    indexes.append(i)
                    break
        return indexes[-1] == n - 1
        
        
        tree = Trie()
        for word in wordDict:
            tree.add(word)
        n = len(s)
        def check(index):
            if index == n:
                return True
            curr = tree.root
            while curr and index < n:
                pos = ord(s[index]) - ord("a")
                curr = curr.children[pos]
                if not curr:
                    return False
                if curr.end and check(index + 1):
                    return True
                index += 1
            return False
        return check(0)
                
            