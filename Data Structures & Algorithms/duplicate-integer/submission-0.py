class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i, v in enumerate(nums): 
            if v in d: 
                return True
            else: 
                d[v] = i
        return False 