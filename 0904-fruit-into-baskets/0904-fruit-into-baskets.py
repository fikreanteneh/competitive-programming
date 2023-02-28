class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        count = defaultdict(int)
        maxi = 1
        left = 0
        for right, types in enumerate(fruits):
            count[types] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    count.pop(fruits[left])
                left += 1
            
            maxi = max(maxi, right - left + 1)
        return maxi

        
            
            
        
        