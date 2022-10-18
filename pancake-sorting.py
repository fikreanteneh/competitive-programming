class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []
        n = len(arr)
        
        for i in range(n-1,-1,-1):
            j = arr.index(i+1)
            if i == 0:
                answer.append(i+1)
                arr[0: i+1] = reversed(arr[0: i+1])
            elif i != j :
                answer.append(j+1)
                arr[0: j+1] = reversed(arr[0: j+1])
                answer.append(i+1)
                arr[0: i+1] = reversed(arr[0: i+1])
        return answer
