class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        def nextWord(word):
            answer = []
            for nextt in wordList:
                differ = 0
                for let1, let2 in zip(word, nextt):
                    if let1 != let2:
                        differ += 1
                if differ == 1:
                    answer.append(nextt)
            wordList.difference_update(answer)
            return answer
                    
        que = deque([beginWord])
        
        if endWord not in wordList:
            return 0
        answer = 1
        while que:
            length = len(que)
            for _ in range(length):
                word = que.pop()
                if word == endWord:
                    return answer
                neigh = nextWord(word)
                que.extendleft(neigh)
            answer += 1
        return 0
                
        