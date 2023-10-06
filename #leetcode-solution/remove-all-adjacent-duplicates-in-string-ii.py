class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        answer = [[""]]
        
        
        for letter in s:
            if len(answer[-1]) == k:
                answer.pop()
            if answer[-1][-1] == letter:
                answer[-1].append(letter)
            else:
                answer.append([letter])
        if len(answer[-1]) == k:
                answer.pop()
        answer = [ "".join(word) for word in answer]
        return "".join(answer)
                