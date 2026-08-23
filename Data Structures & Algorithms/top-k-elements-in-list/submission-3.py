class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} 
        for i in nums:
            if i in d: 
                d[i] += 1
            else: 
                d[i] = 1
       
        val = sorted(d, key=d.get)
    
        return val[-k:]

                
