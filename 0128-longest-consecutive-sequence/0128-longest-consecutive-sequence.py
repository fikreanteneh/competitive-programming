class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Brilliant Solution
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
        # Union FInd Approach
        parents = {}
        ranks = defaultdict(lambda: 1)
        
        def find(num):
            parent = parents[num]
            if parent == num:
                return parent
            parents[num] = find(parent)
            return parents[num]
        
        def union(num1, num2):
            p1 = find(num1)
            p2 = find(num2)
            if p1 == p2:
                return
            if ranks[p2] > ranks[p1]:
                p1, p2 = p2, p1
                num1, num2 = num2, num1
            
            ranks[p1] += ranks[p2]
            parents[p2] = p1
            parents[num2] = p1
            
        for num in nums:
            if num not in parents:
                parents[num] = num
            if num - 1 in parents:
                union(num - 1, num)
            if num + 1 in parents:
                union(num, num + 1)
        answer = 0
        for parent in parents:
            answer = max(answer, ranks[parent])
        return answer