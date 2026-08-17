class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count_0 = nums.count(0)
        # ordered = sorted(nums)
        # ordered.remove(0 * count_0)
        # print(ordered)
        print(count_0)
        
        x = [i for i in nums if i !=0 ]
        print(x)
        x.extend([0] * count_0)
        nums[:] = x




        """
        Do not return anything, modify nums in-place instead.
        """
        