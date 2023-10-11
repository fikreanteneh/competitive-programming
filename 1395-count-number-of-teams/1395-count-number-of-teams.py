class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        store = [[0,0] for _ in range(n)] #Greater, Smaller
        answer = 0
        for i in range(n):
            right = rating[i]
            for j in range(i - 1, -1, -1):
                left = rating[j]
                if right > left:
                    store[i][0] += 1
                    answer += store[j][0]
                elif right < left:
                    store[i][1] += 1
                    answer += store[j][1]
        
        return answer
                        
                
                
        