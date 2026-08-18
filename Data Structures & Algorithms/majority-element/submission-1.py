class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in d:
                d[nums[i]] += 1
                
            else:
                d[nums[i]] = 1
            if d[nums[i]] > n/2:
                    return nums[i]