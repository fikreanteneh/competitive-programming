class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = floor(minutesToTest / minutesToDie) + 1
        answer = math.log(buckets, rounds)
        answer = round(answer, 5)
        answer = ceil(answer)
        return answer
    
        