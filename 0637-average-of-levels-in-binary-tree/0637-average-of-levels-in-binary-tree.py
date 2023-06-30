# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sums = defaultdict(lambda: [0, 0])
        fringe = deque([(root, 0)])
        maxi = 0
        while fringe:
            node,level = fringe.pop()
            maxi = max(level, maxi)
            sums[level][0] += node.val
            sums[level][1] += 1
            if node.left:
                fringe.appendleft((node.left, level + 1))
            if node.right:
                fringe.appendleft((node.right, level + 1))
                                  
        answer = [0] * (maxi + 1)
        for i, j in sums.items():
            answer[i] = j[0]/j[1]
        return answer
                                  
        

            
            
            