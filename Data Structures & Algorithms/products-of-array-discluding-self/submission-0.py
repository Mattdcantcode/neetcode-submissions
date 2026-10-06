class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        n = len(nums)
        k = [0]*n
        count = 0
        output = [0]*n
       
        for i in range(n):
            if nums[i] == 0:
                k[i] = 1
                count += 1
            else: 
                total = total*nums[i]
            
        if count > 1: 
            return output
        elif count == 1:
            for j in range(n):
                if k[j] == 1:
                    output[j] = total
        else: 
            for k in range(n):
                output[k] = total//nums[k]
        return output
            

