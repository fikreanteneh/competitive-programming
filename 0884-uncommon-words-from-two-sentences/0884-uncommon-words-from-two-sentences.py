class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = Counter( s1.split(" ") + s2.split(" ") )
        print(s1.split(" ") + s2.split(" "))
        answer = []
        for word, c in words.items():
            if c == 1:
                answer.append(word)
        return answer