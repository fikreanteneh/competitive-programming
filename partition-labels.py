class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        partitions = [(0,0)]
        for i in range(len(s)):
            if s[i] in index:
                index[s[i]] = (index[s[i]][0], i)
            else:
                index[s[i]] = (i,i)
        
        for j in index:
            if index[j][0] > partitions[-1][-1]:
                partitions.append((index[j][0],index[j][-1]))
            elif partitions[-1][0] <= index[j][0] and index[j][-1] > partitions[-1][-1]:
                partitions[-1] = ( partitions[-1][0], index[j][-1])
        for k in range (len(partitions)):
            partitions[k] = partitions[k][-1] - partitions[k][0] + 1
        return partitions
