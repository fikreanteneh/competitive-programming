class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        count = len(t)  
        sCount = defaultdict(int)
        left = 0
        ans = ""
        cur = float("inf")
        
        for right, lett in enumerate(s):
            sCount[lett] += 1
            
            if sCount[lett] <= tCount[lett]:
                count -= 1
                    
            while not count:
                if right - left + 1 < cur:
                    cur = right -left + 1
                    ans = s[left: right + 1]
                    
                sCount[s[left]] -= 1
                if sCount[s[left]] < tCount[s[left]]:
                    count += 1
                left += 1                 
        return ans
                    
                
        
        