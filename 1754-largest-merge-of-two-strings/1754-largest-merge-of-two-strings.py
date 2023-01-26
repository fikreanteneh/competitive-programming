class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        index1 = 0
        index2 = 0
        merge = []
        while index1 < n and index2 < m:
            if word1[index1] > word2[index2]:
                merge.append(word1[index1])
                index1 += 1
            elif word1[index1] < word2[index2]:
                merge.append(word2[index2])
                index2 += 1
            else:
                if word1[index1:] >= word2[index2:] :
                    merge.append(word1[index1])
                    index1 += 1
                elif word1[index1:] < word2[index2:]:
                    merge.append(word2[index2])
                    index2 += 1          
        merge.append(word1[index1:])
        merge.append(word2[index2:])
        return "".join(merge)
    
                