class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()
        dec = deque()
        maxi = 0
        n = len(nums)
        left = 0
        for right in range(n):
            while inc and inc[-1] > nums[right]:
                inc.pop()
            inc.append(nums[right])
            while dec and dec[-1] < nums[right]:
                dec.pop()
            dec.append(nums[right])
            while left < right and abs(inc[0] - dec[0]) > limit:
                if nums[left] == inc[0]:
                    inc.popleft()
                if nums[left] == dec[0]:
                    dec.popleft()
                left += 1
            # print(left, right, inc, dec)
            maxi = max(maxi, right - left + 1)
        
        
        return maxi
        