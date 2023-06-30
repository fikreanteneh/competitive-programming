class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        # print(nums)
        n = len(nums)
        for x, num in enumerate(nums):
            if num >= 0:
                break
            if num == nums[x-1]:
                continue
            i, j = x+1, n - 1
            while i < j:
                # if i==x: 
                #     i += 1
                # print(x, num, "indexes", i, j)
                left , right = nums[i], nums[j]
                sums = left + right
                if sums == abs(num):
                    ans.append([num, left, right])
                    i+=1
                    j-=1
                    i = self.calculate(nums, i, 1, n)
                    j = self.calculate(nums, j, -1, n)
                elif sums > abs(num):
                    j-=1
                    j = self.calculate(nums, j, -1, n)
                else:
                    i+=1
                    i = self.calculate(nums, i, 1, n)
                    
                # print(ans)
                
        z = 0
        for i in range(x,n):
            if nums[i] != 0:
                break
            z+=1
        if z >= 3: ans.append([0,0,0])
        return ans
    def calculate(self, nums, x, y, n):
        while 0 < x < n and nums[x] == nums[x + (-1 * y)]:
            x+=y
        return x
        # i, j = 0, len(nums) - 1
        # if check.get(0, 0) > 2: 
        #     ans.append([0,0,0])
        # while i < j and nums[i] != 0 and nums[j]!=0:
        #     left, right = nums[i], nums[j]
        #     sums = left + right
        #     remain = 0-sums
        #     exist = check.get(remain, 0)
        #     if left == remain or right == remain:
        #         exist -= 1
        #     if exist > 0:
        #         ans.append([left, remain, right])
        #     if sums > 0:
        #         j-=1
        #     elif sums < 0:
        #         i+=1
        #     else:
        #         i+=1
        #         j-=1
        # return ans
            
                    
        # nega, zero, pos = [], 0, []
        # ans = []
        # for i in nums:
        #     if i == 0: zero += 1
        #     elif i > 0: pos.append(i)
        #     else: nega.append(i)
        # nega.sort()
        # pos.sort()
        # if zero >= 3: ans.append([0,0,0])
        # return [[]]
        """
        0    0
                    0 1 3 8
        -4 -2 -1 -1 0 1 2 5
        
        -4 -1 -1 0 1 2
        
        [[-4,-1,5],[-2,0,2],[-1,-1,2],[-1,0,1]]
        """