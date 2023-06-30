# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        answer = []
        que = deque([(root, 0, 0, "R")])
        id = 0
        while que:
            node, parent, nodeId, dx = que.popleft()
            if not node:
                continue
            answer.append(str(nodeId) + "|" + str(parent) + "|" + str(node.val) + "|" + dx )
            que.append((node.left, nodeId, id + 1, "L"))
            que.append((node.right, nodeId, id + 2, "R"))
            id += 2
        answer = list(answer)
        return " ".join(answer)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None        
        trees = {}
        data = data.split(" ")
        n = len(data)
        nodeId, parent, val, dx = data[0].split("|")
        trees[int(nodeId)] = TreeNode(int(val))
        for i in range(1, n):
            nodeId, parent, val, dx = data[i].split("|")
            trees[int(nodeId)] = TreeNode(int(val))
            if dx == "L": trees[int(parent)].left = trees[int(nodeId)]
            else: trees[int(parent)].right = trees[int(nodeId)]
        return trees[0]
            
            
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))