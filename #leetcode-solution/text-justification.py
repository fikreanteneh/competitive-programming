class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        answer = []
        
        def distributer(i,j, space, length , last):
            if last:
                ans = [words[i]]
                for k in range(i + 1, j):
                    s = " "
                    ans.append(s)
                    ans.append(words[k])
                extra = (maxWidth - (length + space))
                ans.append(" " * extra)
                answer.append("".join(ans))
            
            else:
                spaceNeeded = (maxWidth - length) //  space
                extra = (maxWidth - length) %  space
                ans = [words[i]]
                for k in range(i + 1, j):
                    s = " "*(spaceNeeded) if k - i > extra else " "*(spaceNeeded + 1)
                    ans.append(s)
                    ans.append(words[k])
                answer.append("".join(ans))
                    
                
        i = 0    
        while i < n:
            j = i + 1
            sums = len(words[i])
            space = 0
            while j < n and (sums + len(words[j]) + space + 1) <= maxWidth:
                sums += len(words[j])
                space += 1 
                j += 1
            last = True if j >= n or space == 0 else False 
            distributer(i, j, space, sums, last)
            i = j
        return answer
                
        