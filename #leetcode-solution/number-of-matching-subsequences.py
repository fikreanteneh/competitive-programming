# class Node:
#     def __init__(self):
#         self.child = [None]*26
#         self.end = False

# class Trie:

#     def __init__(self):
#         self.root = Node()
    
#     def charToIndex(self, char):
#         return ord(str(char)) - 97
    
#     def indexToChar(self, index):
#         return chr(index + 97)
    
#     def reachNode(self, value, root = None):
#         curr = root if root else self.root
#         parent, index = curr, -1
#         for i, val in enumerate(value):
#             index = self.charToIndex(val)
#             if curr.child[index] is None:
#                 return (None, None, -1)
#             parent = curr
#             curr = curr.child[index]
#         return (curr, parent, index)

#     def insert(self, value: str) -> None:
#         curr = self.root
#         for i, val in enumerate(value):
#             index = self.charToIndex(val)
#             if curr.child[index] is None:
#                 curr.child[index] = Node()
#             curr = curr.child[index]
#         curr.end = True

#     def search(self, value: str, root = None) -> bool:
#         root = root if root else self.root
#         curr, parent, index = self.reachNode(value, root)
#         return curr and curr.end
        

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        #Trie
        
#         tree = Trie()
#         check = [0]
#         for word in words:
#             tree.insert(word)
#             check.append(tree.root)
#         for i, lett in enumerate(s):
#             index = tree.charToIndex(lett)
#             for j, node in enumerate(check):
#                 if node.child[index]
            
#         def dfs(index, node):
            
#             for i in range(index, n):
#                 if 
        
#         visited = []
        
        
        
        # Binary Search
        ans = 0
        checker = defaultdict(list)
        for i, lett in enumerate(s):
            checker[lett].append(i)
        for word in words:
            index = -1
            flag = True
            for i, lett in enumerate(word):
                index = bisect.bisect_left(checker[lett], index + 1)
                if index == len(checker[lett]):
                    flag = False
                    break
                index = checker[lett][index]
            if flag:
                ans += 1
        return ans