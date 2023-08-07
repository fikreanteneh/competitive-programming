
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
        
    def search(self, value: str) -> bool:
        new = self.root
        length = len(value)
        for i in range (length):
            index = ord(value[i]) - 97
            if new.child[index] is None:
                return False
            new = new.child[index]
        return new.end
    

    def delete(self, value) -> None:
        value = self.wordToListNumber(value)
        stack = [self.root]
        for index in value:
            stack.append(stack[-1].child[index])
        while value:
            node = stack.pop()
            index = value.pop()
            node.end = False
            if any(node.child):
                return
            if stack[-1].end:
                return
            stack[-1].child[index] = None

            
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # tree = Trie()
        # for word in wordDict:
        #     tee.insert(word)
        wordDict = set(wordDict)
        last = {-1:[]}
        for i,char in enumerate(s):
            temp = []
            for index in last.keys():
                word = s[index + 1: i + 1]
                if word in wordDict:
                    temp.append(index + 1)
            if temp:
                last[i] = temp
        stack = []
        answer = []
        def dfs(index):
            if index == -1:
                new = stack.copy()
                new.reverse()
                answer.append(" ".join(new))
                return
            for nextt in last[index]:
                stack.append(s[nextt : index + 1])
                dfs(nextt - 1)
                stack.pop()
            
            
        
        if len(s) - 1 in last:
            dfs(len(s) - 1)
        return answer
                    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        