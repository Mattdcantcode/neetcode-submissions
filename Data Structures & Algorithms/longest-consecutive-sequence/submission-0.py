class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        d = {}
        best = 0
        for v in nums:
            if v - 1 in nums: 
                continue 
            current = v
            length = 1
            while (current+1) in nums: 
                current += 1
                length += 1
            best = max(best,length)
        return best
                