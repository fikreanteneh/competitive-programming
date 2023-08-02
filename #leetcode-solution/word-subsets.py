class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        reach = {}
        for word in words2:
            word = Counter(word)
            for letter, repeated in word.items():
                reach[letter] = max(reach.get(letter, 0), repeated)
        
        answer = []
        for word in words1:
            letter = Counter(word)
            flag = True
            for lett, repeated in reach.items():
                if repeated > letter.get(lett, 0):
                    flag = False
                    break
            if flag:
                answer.append(word)
        
        return answer
            
        