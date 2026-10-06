class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i, char in enumerate(nums):
            d[char] = d.get(char,0)+1
            if d[char] > 1:
                return True
        return False