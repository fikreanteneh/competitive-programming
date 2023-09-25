class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        scores.append(0)
        ages.append(0)
        combined = [(age, score) for age, score in zip(ages, scores)]
        combined.sort()
        n = len(scores)
        store = [0]
        for i in range(1, n):
            age, score = combined[i]
            maxi = 0
            for j in range(i):
                age2, score2 = combined[j]
                if  score2 <= score:
                    maxi = max(maxi, store[j])
            store.append(score + maxi)
        
        return max(store)

                