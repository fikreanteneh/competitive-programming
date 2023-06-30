class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        answer = []
        visited = set()
        heap = [(nums1[0] + nums2[0], 0, 0)]
        n, m = len(nums1), len(nums2)
        while heap and len(answer) < k:
            sums, i, j = heappop(heap)
            if (i, j) in visited:
                continue
            answer.append((nums1[i] , nums2[j]))
            visited.add((i,j))
            if i < n - 1 and (i + 1, j) not in visited:
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            if j < m - 1 and (i, j + 1) not in visited:
                heappush(heap, (nums1[i] + nums2[j + 1], i , j + 1))
        
        return answer