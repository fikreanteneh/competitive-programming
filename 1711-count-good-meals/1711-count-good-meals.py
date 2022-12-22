class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        answer = 0
        nums = dict(Counter(deliciousness))
        multiples = [2**num for num in range(0,22)]
        for i in nums:
            for j in range(21, -1,-1):
                multiple = multiples[j]
                check = multiple - i
                if i == check:
                    value = nums.get(check, 0)
                    answer += ( (value/2) * (value - 1))
                elif i <check:
                    answer += ( nums.get(check, 0) * nums.get(i, 0) )
        return int(answer) % (10**9 + 7)
                    
                    
            
        # nums = dict(Counter(deliciousness))
        # print(nums, math.log(2,2) )
        
        # for i in nums:
        #     if i == 0: continue
        #     if i != 0 and i != 1: 
        #         x = math.log(i,2) 
        #         if x != int(x):
        #             x = x  + 1
        #         # if math.log(i, 2) == int(math.log(i, 2)) else int(math.log(i, 2)) + 1
        #         x =int(x)
        #     else:
        #         x = i
        #     check = 2**x - i
        #     if check == i: 
        #         increase = nums[check]
        #         answer += ((increase/2) *(increase - 1))
        #         answer += (nums.get(0,0)*nums[i])
        #     else: 
        #         answer += ((nums.get(check, 0))*nums[i])
        #     # if i == 1:
        #     #     answer += (nums.get(0,0)*nums[i])
        #     print(answer, i)
        
     