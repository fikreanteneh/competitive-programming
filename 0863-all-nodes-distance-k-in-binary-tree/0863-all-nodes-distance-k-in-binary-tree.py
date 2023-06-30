# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        start = None
        que = deque([(root, None)])
        while que:
            node, par = que.pop()
            if not node:
                continue
            node.neigh = [node.left, node.right, par]
            que.appendleft((node.right, node))
            que.appendleft((node.left, node))
        que = deque([target])
        visited = set([target])
        while que and k:
            length = len(que)
            for _ in range(length):
                node = que.popleft()
                for child in node.neigh:
                    if child and child not in visited:
                        visited.add(child)
                        que.append(child)
            k -= 1
        que = list(que)
        for i, val in enumerate(que):
            que[i] = val.val
        return que



        