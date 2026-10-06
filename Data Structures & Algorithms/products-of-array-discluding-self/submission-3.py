class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        total = 1
        for i in range(n-1):
            output[i+1] = output[i]*nums[i]
        for j in reversed(range(1,n)):
            total = total*nums[j]
            output[j-1] = total*output[j-1]
        return output