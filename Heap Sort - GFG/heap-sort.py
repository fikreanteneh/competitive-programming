#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, index, index2 = None):
        # code here
        left, right = 2 * index + 1, 2 * index + 2
        childIndex = right if right < index2 and arr[right] > arr[left] else left
        try:
            while childIndex < index2 and arr[index] < arr[childIndex]:
                arr[index], arr[childIndex] = arr[childIndex], arr[index]
                index = childIndex
                left, right = 2 * index + 1, 2 * index + 2
                childIndex = right if right < index2 and arr[right] > arr[left] else left
        except:
            return
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n-1, -1, -1):
            self.heapify(arr, n, i, n)
            
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        for i in range(n-1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, n, 0, i)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends