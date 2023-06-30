class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lists = [i for i in range(1,n+1)]
        index  = 0 
        while len(lists) > 1:
            index = (index + k - 1) % len(lists)
            lists.pop(index)
            index = index % len(lists)
        return lists[0]