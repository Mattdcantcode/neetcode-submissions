class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in d: 
                j = d[val]
                return [j,i]
            else: 
                d[nums[i]] = i
            

    
                