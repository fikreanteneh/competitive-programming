# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        incode = []
        def dfs(root):
            if not root:
                incode.append("-")
                return
            incode.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return "|".join(incode)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        # print(data)
        if not data:
            return None
        decode = data.split("|")
        # print(decode)
        tree = TreeNode(int(decode[0]))
        stack = [[tree, 2]]
        n = len(decode)
        
        for i in range(1, n):
            # print(stack[-1][0].val)
            newTree = None
            if decode[i] != "-":
                newTree = TreeNode(int(decode[i]))    
            if stack[-1][1] == 2:
                stack[-1][0].left = newTree
            elif stack[-1][1] == 1:
                stack[-1][0].right = newTree
            stack[-1][1] -= 1
            if stack[-1][1] == 0:
                stack.pop()
            if newTree:
                stack.append([newTree, 2])
        
        return tree
            
            
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans