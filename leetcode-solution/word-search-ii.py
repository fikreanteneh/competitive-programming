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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = Trie()
        for word in words:
            tree.insert(word)
        answer = [] 
        n, m = len(board), len(board[0])
        
        
        direction = ((-1,0),(1,0), (0,1),(0,-1))
        def inbound(i,j):
            return -1 < i < n and -1 < j < m
        
        def dfs(node, root):
            x, y = node
            letter = board[x][y]
            self.stack.append(letter)
            self.visited.add(node)
            
            if root.end:
                word = "".join(self.stack)
                answer.append(word)
                tree.delete(word)
                
            for a, b in direction:
                i, j = x + a, y + b
                
                if inbound(i,j) and (i,j) not in self.visited:
                    newLetter = ord(board[i][j]) - 97 
                    if root.child[newLetter]:
                        dfs((i,j),root.child[newLetter])
                    
            self.visited.discard(node)
            self.stack.pop() 
        
        for row in range(n):
            for col in range(m):
                self.stack = []
                self.visited = set()
                letter = ord(board[row][col]) - 97
                if tree.root.child[letter]:
                    dfs( (row, col), tree.root.child[letter])
        
        return answer
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        