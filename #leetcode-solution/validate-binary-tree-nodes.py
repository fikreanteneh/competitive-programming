class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = [i for i in range(n)]
        rank = [1]*n
        def find(node):
            temp = node
            while parents[node] != node:
                node = parents[node]
            while temp != parents[temp]:
                nextt = parents[temp] 
                parents[temp] = node
                temp = nextt
            return node
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            if parent2 != node2:
                return False
            parents[node2] = parent1
            rank[node1] += 1
            rank[node2] -= 1
            return parent1 != parent2
        
        for node, (left, right) in enumerate(zip(leftChild, rightChild)):
            if left > -1:
                if not union(node, left):
                    return False
            if right > -1:
                if not union(node, right):
                    return False
        total = 0
        root = 0
        for node, (parent, childs) in enumerate(zip(parents, rank)):
            total += childs
            if node == parent:
                root += 1
        return total == n and root == 1