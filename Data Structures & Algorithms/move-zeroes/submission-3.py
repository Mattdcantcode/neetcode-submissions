class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count_0 = nums.count(0)
        x = [i for i in nums if i !=0 ]
        x.extend([0] * count_0)
        nums[:] = x